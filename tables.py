from openpyxl import load_workbook
import convertapi
from random import shuffle

convertapi.api_secret = 'Qv4zM1tcFDkYDkza'
schulte_templates = 'schulte.xlsx'
changed_file = 'changed.xlsx'
template_3x3 = "template_3x3"
template_5x5 = "template_5x5"
columns = [chr(i+65) for i in range(20)]

def getSchulteValues(table_size):
  values = [i + 1 for i in range(0, table_size * table_size)]

  for i in range(5):
    shuffle(values)

  rows = []
  for i in range(table_size):
    rows.append(values[table_size * i : table_size * (i + 1)])
  return rows

def saveSchulteTable(table_size, rows, name):
  wb = load_workbook(filename = schulte_templates)
  template_name = ''
  #saving to Excel format
  if (table_size == 3):
    template_name = template_3x3
  elif (table_size == 5):
    template_name = template_5x5

  ws = wb[template_name]

  for i in range(table_size):
    for j in range(table_size):
      ws['{}{}'.format(columns[i], j + 1)] = rows[i][j]

  wb.save(changed_file)
  real_name = '{}.pdf'.format(name)
  result = convertapi.convert('pdf', { 'File': changed_file, 'WorksheetName': template_name })
  result.file.save(real_name)

  return real_name

def getSchulteTable(table_size, name):
  rows = getValues(table_size)
  table = saveTable(table_size, rows, name)
  return table

print(getTable(3, '3x3'))

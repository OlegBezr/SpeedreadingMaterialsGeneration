from random import shuffle

letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A','E','I','O','U', 'Y']

def cleanWord(s):
	if s[-1] not in letters:
		return [s[:-1], s[-1]]
	else:
		return [s, '']

def mixLetters(s):
	if len(s) > 3:
		symb = [i for i in s]
		mid_symb = symb[1:-1]
		shuffle(mid_symb)
		return ''.join([symb[0]] + mid_symb + [symb[-1]])
	else:
		symb = [i for i in s]
		shuffle(symb)
		return ''.join(symb)

def mixLettersClean(s):
	res = cleanWord(s)
	return mixLetters(res[0]) + res[1]

def mixLettersText(text):
	spl = text.split(" ")
	result = [mixLettersClean(i) for i in spl]
	return ' '.join(result)

def hideLetters(s, n):
	symb = [i for i in s]
	pos = [i for i in range(len(s))]
	shuffle(pos)
	chosen_pos = pos[:(len(s) // n)]

	for i in range(len(symb)):
		if i in chosen_pos:
			symb[i] = '#'
	return ''.join(symb)

def hideLettersClean(s, n):
	res = cleanWord(s)
	return hideLetters(res[0], n) + res[1]

def hideLettersText(text, n):
	spl = text.split(" ")
	result = [hideLettersClean(i, n) for i in spl]
	return ' '.join(result)

def hideVowels(s):
	symb = [i for i in s]
	for i in range(len(symb)):
		if symb[i] in vowels:
			symb[i] = '#'
	return ''.join(symb)

def hideVowelsText(text):
	spl = text.split(" ")
	result = [hideVowels(i) for i in spl]
	return ' '.join(result)

def removeVowels(s):
	symb = [i for i in s]

	if len(symb) > 1:
		for i in range(len(symb)):
			if symb[i] in vowels:
				symb[i] = ''
	return ''.join(symb)

def removeVowelsText(text):
	spl = text.split(" ")
	result = [removeVowels(i) for i in spl]
	return ' '.join(result)

text = "My favorite beach is called Emerson Beach. It is very long, with soft sand and palm trees. It is very beautiful. I like to make sandcastles and watch the sailboats go by. Sometimes there are dolphins and whales in the water!"
print(mixLettersText(text))
print()
print(hideLettersText(text, 3))
print()
print(hideVowels(text))
print()
print(removeVowelsText(text))

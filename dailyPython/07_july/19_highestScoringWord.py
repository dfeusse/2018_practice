'''
Highest Scoring Word
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.
'''
import string

def high(x):
	# assign a point to each letter
	# split string into list of words
	# assign a value to each word
	# return the highest word
	alphabetScore = {}
	value = 1
	for i in string.ascii_lowercase:
		alphabetScore[i] = value
		value+=1

	highestWord = ""
	highestScore = 0
	for i in x.split():
		tempScore = 0
		for a in i:
			tempScore += alphabetScore[a]
		if tempScore > highestScore:
			highestScore = tempScore
			highestWord = i
	return highestWord, highestScore



print high('man i need a taxi up to ubud')
print high('what time are we climbing up the volcano')
print high('take me to semynak')

'''
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]
    '''
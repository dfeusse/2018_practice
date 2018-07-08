'''
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
'''
import string

def find_missing_letter(chars):
	alph = list(string.ascii_lowercase) +  list(string.ascii_uppercase)#'abcdefghijklmnopqrstuvwxyz'
	# find first letter in chars
	startingAlphabetList = alph.index(chars[0])
	# slice alph so list starts there
	# do two loops in parallel comparing
	for (a,c) in zip( alph[startingAlphabetList:], chars):
		#print "alphabet: ", a ,"; char: ", c.lower()
		if a != c:
			return a

print find_missing_letter(['a','b','c','d','f'])#, 'e')
print find_missing_letter(['O','Q','R','S'])#, 'P')

'''
def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))

def find_missing_letter(input):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(input[0])
    for i in range(len(input)):
        if not input[i] == alphabet[start+i]:
            return alphabet[start+i]
            '''
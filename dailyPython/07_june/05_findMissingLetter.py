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
	alph = list(string.ascii_lowercase) #'abcdefghijklmnopqrstuvwxyz'
	# find first letter in chars
	startingAlphabetList = alph.index(chars[0].lower())
	# slice alph so list starts there
	# do two loops in parallel comparing
	for (a,c) in zip( alph[startingAlphabetList:], chars):
		#print "alphabet: ", a ,"; char: ", c.lower()
		if a != c.lower():
			return a

print find_missing_letter(['a','b','c','d','f'])#, 'e')
print find_missing_letter(['O','Q','R','S'])#, 'P')
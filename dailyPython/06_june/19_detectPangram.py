'''
Detect Pangram
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''
import string
def is_pangram(s):
	# get a list of the alphabet
	alphabet = list(string.ascii_lowercase)
	# loop through a string, remove from alphabet what's in string
	for i in s:
		if i in alphabet:
			alphabet.remove(i)
	if len(alphabet) > 0:
		return False
	return True

	# check if length > 0, return true or false


pangram = "The quick, brown fox jumps over the lazy dog!"
print is_pangram(pangram)#, True)
'''
Write a function named firstNonRepeatingLetter that takes a string input, and returns the first character
 that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only 
occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character,
but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should 
return 'T'.
'''
def first_non_repeating_letter(string):
	# have characters in a list, normalize to lower
	# loop through each character
	# if it's in the list less than twice,return it
	allChars = [i.lower() for i in string]
	for i in string:
		if allChars.count(i.lower()) < 2:
			return i
	return ""

print first_non_repeating_letter('hello world, eh?')#, 'w')
print first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!')#, ',')
print first_non_repeating_letter('abba')#, '')
print first_non_repeating_letter('aa')#, '')
print first_non_repeating_letter('a')#, 'a')
print first_non_repeating_letter('stress')#, 't')
print first_non_repeating_letter('moonmen')#, 'e')
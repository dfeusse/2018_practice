'''
Counting Duplicates
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''
def duplicate_count(text):
	# get list of all items
	# loop through the text
	# for each, if count is only once, add 1 to a counter
	counter = []
	texts = list(text)
	print texts
	for i in text:
		if texts.count(i.lower()) > 1:
			print i
			counter.append(i)
	#return len(set(counter))
	return len(set([ i for i in list(text) if list(text).count(i) > 1 ]))

print duplicate_count("abcde")#, 0)
print duplicate_count("abcdea")#, 1)
print duplicate_count("indivisibility")#, 1)
print duplicate_count("aabbcde")
print duplicate_count("indivisibility")
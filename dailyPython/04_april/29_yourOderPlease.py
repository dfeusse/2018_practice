'''

Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est"

'''
def your_order(string):
	string = string.split();
	print string
	newDict = {}
	for s in string:
		# for each word, get number out of string, assign key to number
		for i in s:
			if i.isdigit():
				newDict[int(i)] = s
	sortedArray = []
	for key in sorted(newDict.iterkeys()):
		sortedArray.append(newDict[key])
	return sortedArray
	# get integer
	#return [int(i) for i in string if i.isdigit()]


print your_order("is2 Thi1s T4est 3a")
'''
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''
def unique_in_order(iterable):
	array = [i for i in iterable]
	print array
	noDups = []
	currentIndex = 0
	for i in array:
		currentIndex += 1
		if len(array) != currentIndex
			if array[currentIndex+1] != i:
				noDups.append(i)
	return noDups

print unique_in_order('AAAABBBCCDAABBB') #== ['A', 'B', 'C', 'D', 'A', 'B']
print unique_in_order('ABBCcAD')        # == ['A', 'B', 'C', 'c', 'A', 'D']
#print unique_in_order([1,2,2,3,3])
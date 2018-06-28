'''
Unique In Order
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''
def unique_in_order(string):
	uniqueList = []
	# make all a list
	listString = list(string)
	print listString
	# get index of each element
	listIndex = 0
	for i in listString:
		if listIndex +1 < len(listString):
			#print '--------'
			#print listString[listIndex]
			#print listString[listIndex+1]
			if listString[listIndex] != listString[listIndex+1]:
				uniqueList.append(listString[listIndex])
		listIndex += 1
	return uniqueList
	

print unique_in_order('AAAABBBCCDAABBB')# == ['A', 'B', 'C', 'D', 'A', 'B']
print unique_in_order('ABBCcAD')  #       == ['A', 'B', 'C', 'c', 'A', 'D']
print unique_in_order([1,2,2,3,3]) 
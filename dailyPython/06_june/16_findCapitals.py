'''
Find the capitals
Instructions
Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

Example
'''
def capitals(text):
	index = 0
	indexArray = []
	for i in text:
		if i.isupper() == True:
			indexArray.append(index)
		index += 1
	return indexArray



print capitals('CodEWaRs')#, [0,3,4,6] );
print capitals('DaN')
print capitals('dAn fEusse')
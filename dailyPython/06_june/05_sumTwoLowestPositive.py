'''
Create a function that retruns the sum of the two lowest possible numbers given an array
of minimum of 4 integers. no floats or empty arrays will be passed

ex: array [19, 5, 2, 77] -> 7

'''


def twoLowestPostivies(array):
	sortedArray = sorted(array)
	#array.sort()
	return sortedArray[0] + sortedArray[1]

print twoLowestPostivies([19, 5, 2, 77])# -> 7
print twoLowestPostivies([1, 2, 3])# -> 3
print twoLowestPostivies([100, 101, 100000]) #-> 201
print twoLowestPostivies([1,2,300,1,2,300]) # -> 2
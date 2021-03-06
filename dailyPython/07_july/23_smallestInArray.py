'''
Find the smallest integer in the array
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
'''
def find_smallest_int(arr):
	minNum = arr[0]
	for i in arr:
		if i < minNum:
			minNum = i
	return minNum

print find_smallest_int([78, 56, 232, 12, 11, 43])#, 11)
print find_smallest_int([78, 56, -2, 12, 8, -33])#, -33)
print find_smallest_int([0, 1-2**64, 2**64])#, 1-2**64)

def findSmallestInt(arr):
    #sort array
    arr.sort()
    return arr[0] 
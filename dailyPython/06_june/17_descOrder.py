'''
Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221
'''
def descOrder(nums):
	# make a sorted list of indiv ints
	sortedList = sorted([ i for i in str(nums) ])[::-1]
	# ['5', '4', '4', '2', '1']
	# convert list back to integer
	return int("".join(sortedList))

print descOrder(21445)# Output: 54421
print descOrder(145263)# Output: 654321
print descOrder(1254859723) #Output: 9875543221
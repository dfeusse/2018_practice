'''
Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, function should returns 0
'''
def sequence_sum(begin_number, end_number, step):
	startingNum = begin_number;
	nums = []
	while startingNum <= end_number:
		nums.append(startingNum)
		startingNum += step
	return sum(nums)

print sequence_sum(2, 6, 2)#, 12)
print sequence_sum(1, 5, 1)#, 15)
print sequence_sum(1, 5, 3)#, 5)
print sequence_sum(0, 15, 3)#, 45)
print sequence_sum(16, 15, 3)#, 0)
print sequence_sum(2, 24, 22)#, 26)
print sequence_sum(2, 2, 2)#, 2)
print sequence_sum(2, 2, 1)#, 2)
print sequence_sum(1, 15, 3)#, 35)
print sequence_sum(15, 1, 3)#), 0)
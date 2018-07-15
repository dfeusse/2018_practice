'''
Find Maximum and Minimum Values of a List
Your task is to make two functions, max and min (maximum and minimum in PHP) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.

#Examples

max([4,6,2,1,9,63,-134,566]) returns 566
min([-52, 56, 30, 29, -54, 0, -110]) returns -110
max([5]) returns 5
min([42, 54, 65, 87, 0]) returns 0
#Notes

You may consider that there will not be any empty arrays/vectors.
'''
def max(array):
	maxAmount = array[0]
	for i in array:
		if i > maxAmount:
			maxAmount = i
	return maxAmount

def min(array):
	minAmount = array[0]
	for i in array:
		if i < minAmount:
			minAmount = i
	return minAmount

print max([4,6,2,1,9,63,-134,566])
print min([4,6,2,1,9,63,-134,566])
'''
Square(n) Sum
Complete the squareSum/square_sum/SquareSum method so that it squares each number passed into it and 
then sums the results together.

For example:

square_sum([1, 2, 2]) # should return 9
'''
def square_sum(lst):
	return sum([i**2 for i in lst])

print square_sum([1, 2, 2]) #9
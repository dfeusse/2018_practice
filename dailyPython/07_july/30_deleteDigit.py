'''
Simple Fun #79: Delete a Digit
Task
Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example
For n = 152, the output should be 52;

For n = 1001, the output should be 101.
'''
def delete_digit(n):
	# start at zero, since no negatives
	# loop through
	index = 0
	for i in str(n):
		print str(n)[index]


print delete_digit(152)#,52)
print delete_digit(1001)#,101)
print delete_digit(10)#,1)
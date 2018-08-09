'''
A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits.

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
The Challenge:

Your code must return true or false depending upon whether the given number is a Narcissistic number.
'''
def narcissistic( value ):
	# loop through each individual number in total int
	# raise each to len of int
	# sum them
	# if sum == value, return True, else return False
	'''
	total = sum([ int(i) ** len(str(value)) for i in str(value) ])
	if total == value:
		return True
	return False
	'''
	return value == sum([ int(i) ** len(str(value)) for i in str(value) ])

print narcissistic(7)#, True, '7 is narcissistic');
print narcissistic(371)#, True, '371 is narcissistic');
print narcissistic(122)#, False, '122 is not narcissistic')
print narcissistic(4887)#, False, '4887 is not narcissistic')

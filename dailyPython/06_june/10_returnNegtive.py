'''
Return Negative
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Example:

make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
'''
def make_negative(number):
	# should do: return |number| * -1
	if number > 0:
		return number * -1
	return number

print make_negative(1);  # return -1
print make_negative(-5); # return -5
print make_negative(0);  # return 0
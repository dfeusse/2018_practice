'''
Convert number to reversed array of digits
Convert number to reversed array of digits
Given a random number:

C#: long;
C++: unsigned long;
You have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
'''
def convert(number):
	return [int(i) for i in str(number)[::-1]]

print convert(348597) #[7,9,5,8,4,3]

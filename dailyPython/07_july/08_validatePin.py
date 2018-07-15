'''
Regex validate PIN code
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits 
or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False
'''
def validate_pin(string):
	# loop through each item in the string
	# if any arent ints, return false
	# lastly, check if len is 4 or 6
	for i in list(string):
		if isinstance(i, )

	 try:
...         x = int(raw_input("Please enter a number: "))
...         break
...     except ValueError:
...         print "Oops!  That was no valid number.  Try again..."

print validate_pin("1234")# == True
print validate_pin("12345") #== False
print validate_pin("a234")# == False
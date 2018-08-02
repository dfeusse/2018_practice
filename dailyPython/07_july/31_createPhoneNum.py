'''
Create Phone Number
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge. 
Don't forget the space after the closing parentheses!
'''
def create_phone_number(n):
	nn = [str(i) for i in n]
	print nn
	if len(n) == 10:
		numberr = "("
		index = 0
		for i in nn:
			numberr += i
			if index == 2:
				numberr += ") "
			elif index == 5:
				numberr += "-"
			index+=1
	return numberr

print create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])#, "(123) 456-7890")
print create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])#, "(111) 111-1111")
print create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])#, "(123) 456-7890")
print create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])#, "(023) 056-0890")
print create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#, "(000) 000-0000")
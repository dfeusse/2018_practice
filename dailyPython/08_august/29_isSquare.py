'''
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
is_square (-1) # => false
is_square   0 # => true
is_square   3 # => false
is_square   4 # => true
is_square  25 # => true
is_square  26 # => false
'''
def is_square(n):
	#return True if i * i == n for i in range(0,n+1) else False 
	for i in range(0,n+1):
		if i * i == n:
			return True
	return False


print is_square(-1)#, #False, "-1: Negative numbers cannot be square numbers")
print is_square(0)#, True, "0 is a square number")
print is_square( 3)#, False, "3 is not a square number")
print is_square( 4)#, True, "4 is a square number")
print is_square(25)#, #True, "25 is a square number")
print is_square(26)#, #False, "26 is not a square number")

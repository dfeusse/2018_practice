'''
create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).

For example:

gimme([2, 3, 1]) => 0
'''
def gimme(input_array):
	originalArray = list(input_array)
	input_array.sort(key=int)
	print input_array
	print originalArray
	return originalArray.index(input_array[1])

print gimme([2, 3, 1])
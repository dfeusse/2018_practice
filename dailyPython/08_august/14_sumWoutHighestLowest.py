'''
Sum without highest and lowest number
Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)

Example:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
'''
def sum_array(arr):
	'''
	if arr == None or len(arr) <= 2:
		return 0
	return sum(sorted(arr)[1:-1])
	'''
	return 0 if arr == None or len(arr) <= 2 else sum(sorted(arr)[1:-1])

print sum_array(None),# 0)
print sum_array([]),# 0)

print sum_array([3])#, 0)
print sum_array([-3])#, 0)

print sum_array([ 3, 5])#, 0)
print sum_array([-3, -5])#, 0)

print sum_array([6, 2, 1, 8, 10])#, 16)
print sum_array([6, 0, 1, 10, 10])#, 17)

print sum_array([-6, -20, -1, -10, -12])#, -28)
print sum_array([-6, 20, -1, 10, -12])#, 3)

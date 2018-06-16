'''
Like my last kata, try to make a function that counts the length of a list, but this time, 
without any of the default len functions, which are removed.
'''
def count(lst):
	listLen = 0
	for i in lst:
		listLen += 1
	#return listLen
	return sum([1 for i in lst])


print count(list([1, 2, 3, 4, 5, 6]))#, 6)
print count([3, 4, 5, 6])
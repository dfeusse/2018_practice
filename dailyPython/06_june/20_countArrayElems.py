'''
Counting Array Elements
Write a function that takes an array and counts the number of each unique element present.

count(['james', 'james', 'john']) 
#=> { 'james' => 2, 'john' => 1}
'''

def count(array):
	pone = {}
	for i in array:
		if i in pone.keys():
			pone[i] += 1
		else:
			pone[i] = 1
	return pone

print count(['a', 'a', 'b', 'b', 'b'])#, { 'a': 2, 'b': 3 })
print count(['james', 'james', 'john']) 
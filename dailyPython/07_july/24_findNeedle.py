'''
A Needle in the Haystack
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Python, Ruby & Elixir

find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
'''
def find_needle(haystack):
	index = 0
	for i in haystack:
		if i == "needle":
			return "found the needle at position " + str(index)
		index+=1

print find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])#, 3)
print find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
print find_needle([1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54])#, 30)


def find_needle(haystack): 
	return 'found the needle at position %d' % haystack.index('needle')

def find_needle(haystack):
    for i, x in enumerate(haystack):
        if x == 'needle': 
            return 'found the needle at position %d' % i
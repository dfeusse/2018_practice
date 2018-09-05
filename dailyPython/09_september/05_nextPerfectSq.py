'''
Find the next perfect square!
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
'''

def findNextSquare(integer):
	for i in range(integer-1):
		if i ** 2 == integer:
			return (i+1) ** 2
	return -1

print findNextSquare(121)# --> returns 144
print findNextSquare(625)# --> returns 676
print findNextSquare(114)# --> return -1


def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1


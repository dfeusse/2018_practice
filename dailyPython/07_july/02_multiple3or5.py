'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
'''
def solution(number):
	# get a list of numbers from number down to 3
	# check if each is a multiple of 3 or 5
	# append to list if it is
	# sum all numbers
	mults = []
	for i in range(3,number):
		if i % 3 == 0 or i % 5 == 0:
			mults.append(i)
	#return sum(mults)
	return sum([i for i in range(3, number) if i % 3 == 0 or i % 5 == 0 ])

print solution(10)#, 23
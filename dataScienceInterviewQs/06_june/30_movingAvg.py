'''
Calculating a moving average using python
You are given a list of numbers J and a single number p.
Write a function to return the minimum and maximum averages of the sequences of p numbers in J. 
Example:

J = [4, 4, 4, 9, 10, 11, 12]

p = 3

The sequences will be:

(4,4,4)

(4,4,9)

(4,9,10)

(9,10,11)

(10,11,12)


Minimum average will be 4 and the maximum average will be 11, which corresponds to the first and last sequences.
'''

def movingAvg(sequence, lenMovingAvg):
	# get a list of each sequence, with the right length
	index = 0
	averages = []
	for i in sequence:
		eachSequence = sequence[index:index+lenMovingAvg]
		if len(eachSequence) == lenMovingAvg:
			# avg of each sequence
			averages.append( sum(eachSequence)/len(eachSequence) )
			#print eachSequence
		index += 1
	return min(averages), max(averages)

print movingAvg([4, 4, 4, 9, 10, 11, 12], 3)

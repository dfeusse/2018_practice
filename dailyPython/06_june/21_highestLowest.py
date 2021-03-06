'''
Highest and Lowest
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
'''
def high_and_low(string):
	listInts = sorted([int(i) for i in string.split()])
	return str(listInts[-1]) + " " + str(listInts[0])

print high_and_low("1 2 3 4 5")  # return "5 1"
print high_and_low("1 2 -3 4 5") # return "5 -3"
print high_and_low("1 9 3 4 -5") # return "9 -5"
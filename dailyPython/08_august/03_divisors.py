'''
Find the divisors!
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
'''
def divisors(integer):
	# loop through list of ints starting with 1 lower than number to 2
	# return list of all that are divisors
	divisors = []
	for i in range(2,integer):
		if integer % i == 0:
			divisors.append(i)
	if len(divisors) == 0:
		return str(integer) + " is prime"
	return divisors

print divisors(15)#, [3, 5]);
print divisors(12)#, [2, 3, 4, 6]);
print divisors(13)#, "13 is prime");
'''
Find the divisors!
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
'''
def divisors(integer):
	#return [i for i in range(2, integer) if integer % i == 0]
	return str(i+1) + ' is prime' if len([i for i in range(2, integer) if integer % i == 0]) == 0 else [i for i in range(2, integer) if integer % i == 0]
	# need to find all the divisors
	# not include 1 or the integer
	# divide int by each number, except 1 or int, and if remainder is 0, add to a list
	answers = []
	for i in range(2, integer):
		if integer % i == 0:
			answers.append(i)
	if len(answers) == 0:
		return str(integer) + " is prime"
	return answers


print divisors(12); #should return [2,3,4,6]
print divisors(25); #should return [5]
print divisors(13); #should return "13 is prime"
print divisors(15); #should return [5,3]
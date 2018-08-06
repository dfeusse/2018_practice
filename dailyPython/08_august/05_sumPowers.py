'''
The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Let's see some cases:

sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_dig_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
'''

def sum_dig_pow(a, b):
	# loop through numbers in range of aruguments given
	# check requirements, loop through each digit of number
	# if num meets requirements, append to list
	answer = []
	for i in range(a, b+1):
		intSum = 0
		power = 1
		for z in str(i):
			intSum = intSum + int(z) ** power
			power += 1
		if intSum == i:
			answer.append(i)
	return answer

print sum_dig_pow(1, 10)#, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print sum_dig_pow(1, 100)#, [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
'''
print sum_dig_pow(10, 89)#,  [89])
print sum_dig_pow(10, 100)#,  [89])
print sum_dig_pow(90, 100)#, [])
print sum_dig_pow(89, 135)#, [89, 135])
'''

def sum_dig_pow(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    res = []
    for number in range(a, b+1):
        digits = [int(i) for i in str(number)]
        s = 0
        for idx, val in enumerate(digits):
            s += val ** (idx + 1)
        if s == number:
            res.append(number)
    return res
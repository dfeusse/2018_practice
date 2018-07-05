'''
Largest 5 digit number in a series
In the following 6 digit number:

283910
91 is the greatest sequence of 2 consecutive digits.

In the following 10 digit number:

1234567890
67890 is the greatest sequence of 5 consecutive digits.

Complete the solution so that it returns the greatest sequence of five consecutive digits 
found within the number given. The number will be passed in as a string of only digits. 
It should return a five digit integer. The number passed may be as large as 1000 digits.
'''
def solution(digits):
	answer = 0
	index = 0
	for i in str(digits):
		if len(str(digits)[index:index+5]) == 5:
			if int(str(digits)[index:index+5]) > answer:
				answer = int(str(digits)[index:index+5])
		index+=1
	return answer

print solution(1234567890) #67890

'''
def solution(digits):
    numlist = [int(digits[i:i+5]) for i in range(0,len(digits)-4)]
    return max(numlist)


def solution(digits):
    result = -1;
    for i in range(len(digits)):
        current = int(digits[i: i+5])
        if current >= result:
            result = current
    return result
    '''
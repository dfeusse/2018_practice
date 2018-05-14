'''
Given few numbers, you need to print out the digits that are not being used.

Example:

unused_digits(12, 34, 56, 78) # "09"
unused_digits(2015, 8, 26) # "3479"
Note:

Result string should be sorted
The test case won't pass Integer with leading zero
'''
def unused_digits(*nums):
	existingNums = []
	for i in nums:
		for z in str(i):
			existingNums.append(int(z))

	unusedDig = ""
	for i in range(10):
		if i not in existingNums:
			unusedDig = unusedDig + str(i)

	return unusedDig


print unused_digits(12, 34, 56, 78) # "09"
print unused_digits(2015, 8, 26) # "3479"

'''
def unused_digits(*l):
    digits_set = set(list("0123456789"))
    test_set = set("".join(str(i) for i in l))
    d = digits_set.difference(test_set)
    r = "".join(sorted(d))
    return r

def unused_digits(*args):
    return "".join(number for number in "0123456789" if number not in str(args))
    '''

digits_set = set(list("0123456789"))
print digits_set
l = 12, 34, 56, 78
print l
print "".join(str(i) for i in l)
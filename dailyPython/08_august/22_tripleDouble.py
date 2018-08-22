'''
which takes in numbers num1 and num2 and returns 1 if there is a straight triple of a number
 at any place in num1 and also a straight double of the same number in num2.
For example:
triple_double(451999277, 41177722899) == 1 // num1 has straight triple 999s and 
                                          // num2 has straight double 99s
triple_double(1222345, 12345) == 0 // num1 has straight triple 2s but num2 has only a single 2

'''
def triple_double(num1, num2):
	num = ""
	for count, ele in enumerate(str(num1)):
		try:
			if ele == str(num1)[count + 1] and ele == str(num1)[count + 2]:
				num = ele
		except IndexError:
			num += ""
	if list(str(num2)).count(num) == 2:
		return 1
	return 0


print triple_double(451999277, 41177722899)#, 1)
print triple_double(1222345, 12345)#, 0)
print triple_double(12345, 12345)#, 0)
print triple_double(666789, 12345667)#, 1)
print triple_double(10560002, 100)#, 1)

def triple_double(num1, num2):
    for x in range(10):
        if str(x) * 3 in str(num1):
            if str(x) * 2 in str(num2):
                return 1
    return 0
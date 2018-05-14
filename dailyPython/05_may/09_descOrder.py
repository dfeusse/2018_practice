'''
Your task is to make a function that can take any non-negative integer as a argument 
and return it with its digits in descending order. Essentially, rearrange the digits 
to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221
'''
def Descending_Order(num):
	return int("".join(sorted(list(str(num)), reverse=True)))

print Descending_Order(0)#, 0)
print Descending_Order(15)#, 51)
print Descending_Order(123456789)#, 987654321)

'''
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)
    '''
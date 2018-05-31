'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
 insensitive. The string can contain any char.

Examples input/output:

print XO("ooxx") #=> true
print XO("print xooxx") #=> false
print XO("ooxXm") #=> true
print XO("zpzpzpp") #=> true // when no 'x' and 'o' is present should return true
print XO("zzoo") #=> false
'''
def XO(s):
    #return True
    numXs = 0
    numOs = 0
    for i in s:
    	if i == 'x' or i == 'X':
    		numXs += 1
    	elif i == 'o' or i == 'O':
    		numOs += 1
    if numOs == numXs:
    	return True
    else:
    	return False


print XO('print xo')#, 'True expected')
print XO('print xo0')#, 'True expected')
print XO('xxprint xoo')#, 'False expected')

print XO("ooxx") #=> true
print XO("print xooxx") #=> false
print XO("ooxXm") #=> true
print XO("zpzpzpp") #=> true // when no 'x' and 'o' is present should return true
print XO("zzoo") #=> false
'''
Question 20 - One edit away
Write a function to return a boolean that indicates if two strings are one edit away from being identical. 
The function should take in 2 strings and return a boolean. The definition of an "edit" is as follows:

Insert one character
Remove one character
Replace one character
A few examples of inputs and the function result are listed below.

        
OneEditAway("pea", "peas") = True

        
OneEditAway("pea", "fleas") = False

        
OneEditAway("pea", "lea") = True

        
OneEditAway("pea", "seas") = False
'''
def OneEditAway(inp1, inp2):
	# all diff is one char
	# loop through one list
	# see if that's in a list
	# more so, must remove it in case of dups
	# if more than one not there, return false
	diffs = 0
	array = list(inp2)
	#print array
	for i in list(inp1):
		#print i
		if i not in array:
			diffs += 1
		else:
			array.remove(i)
		#print array
	print array
	if len(array) > 1:
		return False
	return True

print OneEditAway("pea", "peas")# = True  
print OneEditAway("pea", "fleas")# = False  

print OneEditAway("pea", "lea")# = True  
print OneEditAway("pea", "seas")# = False

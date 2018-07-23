'''
Split Strings
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''

def solution(s):
	if len(s) % 2 != 0:
		s +='_'
	tup = zip(s[::2], s[1:][::2])
	return [ str(i[0]) + str(i[1]) for i in tup]

print solution("asdfadsf")#, ['as', 'df', 'ad', 'sf']),
print solution("asdfads")#, ['as', 'df', 'ad', 's_']),
print solution("")#, []),
print solution("x")#, ["x_"]),

'''
def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]
    '''
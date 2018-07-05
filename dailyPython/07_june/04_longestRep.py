'''
For a given string s find the character c with longest consecutive repetition and return a tuple (c, l) 
'''
def longest_repetition(chars):
	largest = {}
	temp = {}
	for i in chars:
		


# longest_repetition[input,) expected],
print longest_repetition("aaaabb")#, ('a', 4)],
print longest_repetition("bbbaaabaaaa")#, ('a', 4)],
print longest_repetition("cbdeuuu900")#, ('u', 3)],
print longest_repetition("abbbbb")#, ('b', 5)],
print longest_repetition("aabb")#, ('a', 2)],
print longest_repetition("ba")#, ('b', 1)],
print longest_repetition("",)# ('', 0)],
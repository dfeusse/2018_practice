'''
print Where my anagrams at?
print What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false
print Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

print anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

print anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

print anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
'''
def anagrams(a, array):
	answer = []
	for i in array:
		if "".join(sorted(a)).lower() == "".join(sorted(i)).lower():
			answer.append(i)
	return [i for i in array if "".join(sorted(a)).lower() == "".join(sorted(i)).lower()]
	#return answer


print anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])# => ['aabb', 'bbaa']

print anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) #=> ['carer', 'racer']

print anagrams('laser', ['lazing', 'lazy',  'lacer'])# => []
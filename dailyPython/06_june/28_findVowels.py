'''
We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

Some examples:
Mmmm  => []
Super => [2,4]
Apple => [1,5]
YoMama -> [1,2,4,6]
NOTE: Vowels in this context refers to English Language Vowels - a e i o u y

NOTE: this is indexed from [1..n] (not zero indexed!)

'''
def vowel_indices(word):
	index = 1
	answer = []
	for i in word:
		if i.lower() in ['a', 'e', 'i', 'o', 'u','y']:
			answer.append(index)
		index += 1
	return answer

print vowel_indices('Mmmm')#  => []
print vowel_indices('Super') #=> [2,4]
print vowel_indices('Apple' )#=> [1,5]
print vowel_indices('YoMama')# -> [1,2,4,6]


'''
def vowel_indices(word):
  return [i+1 for i,c in enumerate(word.lower()) if c in 'aeiouy']
  '''
  ''' The enumerate() function adds a counter to an iterable.
  
  my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# Output:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear
'''
Find something in an Array
Create a find function that takes a string and an array as arguments. If the string is in the array, return true.

For example:

findSomething("hello", ["bye bye","hello"]) # return true
findSomething("anything", ["bye bye","hello"]) # return false
'''
def findSomething(word, array):
	for i in array:
		if word == i:
			return True
	return False

print findSomething("hello", ["bye bye","hello"]) # return true
print findSomething("anything", ["bye bye","hello"]) # return false
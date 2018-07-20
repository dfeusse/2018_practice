'''
Reversed Words
Complete the solution so that it reverses all of the words within the string passed in.

Example:

reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"
'''
def reverseWords(str):
	# split words in list
	# loop through list backwards
	# append each word to new list
	# make list into a string
	newWord = ""
	for i in str.split()[::-1]:
		newWord = newWord + " " + i
	return newWord.strip()

print reverseWords("hello world!")#, "world! hello")
print reverseWords("The greatest victory is that which requires no battle")


def reverseWords(str):
    return " ".join(str.split(" ")[::-1])

print reverseWords("hello world!")#, "world! hello")
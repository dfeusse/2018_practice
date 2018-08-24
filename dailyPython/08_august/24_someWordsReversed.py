'''
top gninnipS My sdroW!
Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. Spaces will be included 
only when more than one word is present.


Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
'''
def spin_words(sentence):
	# start with an empty string
	# loop through the sentence
	# if len less than 5, just append word as is
	# if more than 5, reverse word then append
	# clean ends up of any spaces just in case, sometimes can be messy when looping
	answer = ""
	for i in sentence.split():
		if len(i) < 5:
			answer += i + " "
		else:
			answer += i[::-1] + " "
	#return answer.strip()
	return " ".join([ i if len(i) < 5 else i[::-1] for i in sentence.split() ])



print spin_words("Welcome")#, "emocleW")
print spin_words( "Hey fellow warriors" )# => returns "Hey wollef sroirraw" 
print spin_words( "This is a test")# => returns "This is a test" 
print spin_words( "This is another test" )#=> returns "This is rehtona test"
'''
imple Pig Latin
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !
'''
def pig_it(text):
	# loop through each word
	# slice the word except for first letter
	# slice the first letter
	# add together and append 'ay' to end
	# return string of all together
	return " ".join([ i[1:] + i[0] + 'ay' for i in text.split() if i not in '!,."'])

print pig_it('Pig latin is cool')#,'igPay atinlay siay oolcay')
print pig_it('This is my string')#,'hisTay siay ymay tringsay')
print pig_it('Hello world !')  # elloHay orldWay !

def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
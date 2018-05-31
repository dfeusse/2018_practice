'''
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

def reverse_words(text):
	arrayWords = text.split()
	reversedWords = ''
	for i in arrayWords:
		reversedWords = reversedWords + ' ' + i[::-1]
	#return reversedWords
	return "".join([ i[::-1] + " " for i in text.split()])


print reverse_words('The quick brown fox jumps over the lazy dog.')#, 'ehT kciuq nworb xof spmuj revo eht yzal .god')
print reverse_words('apple')#, 'elppa')
print reverse_words('a b c d')#, 'a b c d')
print reverse_words('double  spaced  words')#, 'elbuod  decaps  sdrow')
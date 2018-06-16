'''
altERnaTIng cAsE <=> ALTerNAtiNG CaSe
altERnaTIng cAsE <=> ALTerNAtiNG CaSe
Define String.prototype.toAlternatingCase (or a similar function/method such as 
to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; 
see the initial solution for details) such that each lowercase letter becomes uppercase 
and each uppercase letter becomes lowercase. For example:

"hello world".toAlternatingCase() === "HELLO WORLD"
"HELLO WORLD".toAlternatingCase() === "hello world"
"hello WORLD".toAlternatingCase() === "HELLO world"
"HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
"12345".toAlternatingCase() === "12345" // Non-alphabetical characters are unaffected
"1a2b3c4d5e".toAlternatingCase() === "1A2B3C4D5E"
'''
def to_alternating_case(string):
	finalString = ""
	for i in string:
		print i
		if i.isupper() == True:
			i.lower()
		i.upper()
		print i
		finalString += i
	return finalString

print to_alternating_case("hello world")#.toAlternatingCase() === "HELLO WORLD"
print to_alternating_case("HELLO WORLD")#.toAlternatingCase() === "hello world"
print to_alternating_case("hello WORLD")#.toAlternatingCase() === "HELLO world"
print to_alternating_case("HeLLo WoRLD")#.toAlternatingCase() === "hEllO wOrld"
print to_alternating_case("12345")#.toAlternatingCase() === "12345" // Non-alphabetical characters are unaffected
print to_alternating_case("1a2b3c4d5e")#.toAlternatingCase() === "1A2B3C4D5E"

#str.isupper()
#s.lower())


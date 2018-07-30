'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
'''
def to_camel_case(text):
	# loop through the text
	# if char is - or _ then capitalize the next letter
	split = text.replace("_"," ").replace("-"," ").split()
	return split[0] + "".join( [i[0].upper() + i[1:] for i in split[1:]] )

print to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
print to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
print to_camel_case("the_Stealth_Warrior") # returns "theStealthWarrior"
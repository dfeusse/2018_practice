'''
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
'''
def valid_parentheses(string):
	return string

print valid_parentheses("  (")#,False)
print valid_parentheses(")test")#,False)
print valid_parentheses("")#,True)
print valid_parentheses("hi())(")#,False)
print valid_parentheses("hi(hi)()")#,True)
print valid_parentheses("()")#              =>  true
print valid_parentheses(")(()))")#          =>  false
print valid_parentheses("(")#               =>  false
print valid_parentheses("(())((()())())")
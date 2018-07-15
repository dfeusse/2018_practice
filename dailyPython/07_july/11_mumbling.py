'''
Mumbling
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
def accum(string):
	index = 1
	answer = ""
	for i in string:
		answer += i.upper() + i.lower() * (index-1) + "-"
		index += 1
	return answer[:-1]

print accum("abcd")    # "A-Bb-Ccc-Dddd"
print accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print accum("cwAt")    # "C-Ww-Aaa-Tttt"
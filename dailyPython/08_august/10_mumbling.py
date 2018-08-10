'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
def accum(s):
	# first follows a different pattern so i'd do s[0]
	# then loop through each letter
	# and add - i.upper i.lower * number of loops
	restOfString = ""
	for count, i in enumerate(s[1:],1):
		restOfString += "-" + i.upper() + i.lower()*count
	return s[0].upper() + restOfString

print accum("abcd")# "A-Bb-Ccc-Dddd"
print accum("cwAt")    # "C-Ww-Aaa-Tttt"
'''
print accum("ZpglnRxqenU")#, "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
print accum("NyffsGeyylB")#, "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
print accum("MjtkuBovqrU")#, "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
print accum("EvidjUnokmM")#, "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
print accum("HbideVbxncC")#, "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")
'''
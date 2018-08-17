'''
Write Number in Expanded Form
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!
'''
def expanded_form(num):
	# loop through the number
	# take the first value
	# append appropraite amount of zeros
	# have rest of numbers
	# repeat
	answer = ""
	for index, value in enumerate(str(num), 1):
		#print value, str(num)[index:]
		if value != '0':
			answer = answer + value + '0' * len(str(num)[index:]) + ' + '
	return answer[:-3]

print expanded_form(12)#, '10 + 2');
print expanded_form(357) # 300 + 50 + 7

print expanded_form(42)#, '40 + 2');
print expanded_form(71314) # + 70000 + 1000 + 300 + 10 + 4
print expanded_form(70304)#, '70000 + 300 + 4');

'''
Beginner Series #2 Clock
Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to miliseconds.

1 sec = 1000 millis

#####Example:

past(0, 1, 1) == 61000
'''
def past(h, m, s):
	# need total seconds
	secs = (h * 60 * 60) + (m * 60) + s
	return secs * 1000
	# total seconds * 1000
print past(0,1,1)
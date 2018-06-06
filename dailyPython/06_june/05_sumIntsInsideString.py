'''
task is function that caluclates sum of integers inside a string
ex. "The30quick 020brown10f0xx1203jus914o3er", calculate sum of those ints
'''
def sumInts(string):
	print [int(s) for s in string if s.isdigit()]
	return sum([int(s) for s in string if s.isdigit()])

print sumInts("The30quick 020brown10f0xx1203jus914o3er")
'''
Round to the next multiple of 5.
Given an integer as input, can you round it to the next (meaning, "higher") 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.
Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers.
'''
def round5(num):
	for i in range(num, num+6):
		if i % 5 == 0:
			return i

print round5(0)
print round5(2)
print round5(3)
print round5(12)
print round5(21)
print round5(30)
print round5(-2)
print round5(-5)
print round5(-7)
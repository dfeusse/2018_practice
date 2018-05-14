'''
 Bob observed that one number usually
differs from the others in evenness. Help Bob  check his answers, he needs a program 
that among the given numbers finds one that is different in evenness, and return a position 
f this number.

! Keep in mind that your task is to help Bob solve a real IQ test, 
which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
'''
def iq_test(string):
	oddEvenArray = [ "even" if int(i) % 2 == 0 else "odd" for i in string.split() ]

	if oddEvenArray.count("even") == 1:
		return oddEvenArray.index("even") + 1
	else:
		return oddEvenArray.index("odd") + 1

print iq_test("2 4 7 8 10")# => 3 // Third number is odd, while the rest of the numbers are even

print iq_test("1 2 1 1")
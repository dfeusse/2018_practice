'''
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
'''

def even_or_odd(number):
	if number % 2 != 0:
		return "odd"
	return "even"

print even_or_odd(2)
print even_or_odd(3)

'''
def even_or_odd(number):
  return 'Odd' if number % 2 else 'Even'
  '''
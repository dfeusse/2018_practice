'''
Question 38 - Calculating earnings with Python
Suppose an individual is taxed 30% if earnings for a given week are > = $2,000. 
If earnings land < $2,000 for the week, the individual is taxed at a lower rate of 15%.

Write a function using Python to calculate both the pre-tax and post-tax earnings for a 
given individual, with the ability to feed in the hourly wage and the weekly hours as inputs.

For example, if an individual earns $55/hour and works for 40 hours, the function should return:

Pre-tax earnings were 55*40 = $2,200 for the week.
Post-tax earnings were $2,200*.7 (since we fall in higher tax bracket here) = $1,540 for the week
Solution will be provided in Python to premium users.
'''
def earnings(hourlyWage, weeklyHours):
	preTax = hourlyWage * weeklyHours
	#return preTax *= .70 if preTax >= 2000 else preTax = preTax * .85
	if preTax >= 2000:
		preTax *= .70
	else: 
		preTax *= .85
	return preTax 

print earnings(40, 40)
print earnings(40, 40)
print earnings(50, 40)
print earnings(55, 40)
print earnings(55, 20)
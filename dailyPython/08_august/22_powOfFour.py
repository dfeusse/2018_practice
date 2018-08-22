'''
Power of 4
Write a method that returns true if a given parameter is a power of 4, and false if it's not. If parameter is not an Integer (eg String, Array) method should return false as well.

(In C# Integer means all integer Types like Int16,Int32,.....)

Examples
isPowerOf4 1024 #should return True
isPowerOf4  102 #should return False
isPowerOf4   64 #should return True
'''
def powerof4(n):
	for i in range(n+1):
		print i
		print i ** 4
		print '---------'
		if i ** 4 == n:
			return True
	return False
'''
print powerof4(4)#, True, "Wrong result for 4")

print powerof4(40)#, False, "Wrong result for 40")
print powerof4(1)#, True, "Wrong result for 1")
print powerof4(64)
'''
#print powerof4(1024)
#print powerof4(102)
print powerof4(1)
print powerof4(64)

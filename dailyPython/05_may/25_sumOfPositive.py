'''
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: array may be empty, in this case return 0.
'''
def positive_sum(arr):
	return sum([i for i in arr if i > 0])

print positive_sum([1,2,3,4,5])#,15)
print positive_sum([1,-2,3,4,5])#,13)
print positive_sum([-1,2,3,4,-5])#,9)

#Test.it("returns 0 when array is empty")
print positive_sum([])#,0)

#Test.it("returns 0 when all elements are negative")
print positive_sum([-1,-2,-3,-4,-5])#,0)

'''
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
    
def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))
'''
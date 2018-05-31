'''
Write a function that takes an array and counts the number of each unique element present.

count(['james', 'james', 'john']) 
#=> { 'james' => 2, 'john' => 1}
'''
def count(array):
    #your code here
    outputDict = {}
    for i in array:
    	if i not in list( outputDict.keys() ):
    		outputDict[i] = 1
    	else:
    		outputDict[i] += 1
    return outputDict

print count(['a', 'a', 'b', 'b', 'b'])#, { 'a': 2, 'b': 3 })
print count(['james', 'james', 'john']) #=> { 'james' => 2, 'john' => 1}

'''
def count(array):
    result = {}
    for x in array:
        result[x] = result.get(x, 0) + 1
    return result

 def count(array):
    return {x: array.count(x) for x in array}
    '''
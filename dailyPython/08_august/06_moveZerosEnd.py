'''
Moving Zeros To The End
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
'''
def move_zeros(array):
	zeros = []
	original = []
	for i in array:
		if i == 0:
			zeros.append(i)
		else:
			original.append(i)
	#return original + zeros
	return [i for i in array if i != 0] + [i for i in array if i == 0]

print move_zeros([False,1,0,1,2,0,1,3,"a"])
print move_zeros([1,2,0,1,0,1,0,3,0,1])#,[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
print move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])#,[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
print move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9])#,["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
print move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])#,["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
print move_zeros([0,1,None,2,False,1,0])#,[1,None,2,False,1,0,0])
print move_zeros(["a","b"])#,["a","b"])
print move_zeros(["a"])#,["a"])
print move_zeros([0,0])#,[0,0])
print move_zeros([0])#,[0])
print move_zeros([])#,[])

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
    
def move_zeros(array):
     return [a for a in array if isinstance(a, bool) or a != 0] + [a for a in array if not isinstance(a, bool) and a == 0]
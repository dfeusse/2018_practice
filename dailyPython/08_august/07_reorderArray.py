'''
Reorder Array
This kata focuses on the Numpy python package and you can read up on the Numpy sorting functions here: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.sort.html#sorting

You will get two inputs, an array arr and an integer n. You must return the array so that value of the element in the n-th position is in the position it would be in a sorted array. Integers smaller than the value of the element in the n-th position are moved before it, and all integers greater than are moved after it. Four examples are shown below:

reorder([6, 5, 8, 1, 7, 2, 9, 3, 4],2) == [1, 2, 3, 6, 7, 5, 9, 8, 4]
reorder([7, 3, 9, 6, 2, 5, 1, 8, 4],5) == [3, 2, 1, 4, 5, 6, 7, 8, 9]
reorder([2, 9, 1, 5, 7, 3, 6, 4, 8],5) == [2, 1, 3, 4, 5, 6, 7, 9, 8]
reorder([6, 2, 4, 9, 1, 3, 7, 8, 5],5) == [2, 1, 4, 3, 5, 6, 7, 8, 9]
'''
def reorder(arr, n):


print reorder([6, 5, 8, 1, 7, 2, 9, 3, 4],2)#,[1, 2, 3, 6, 7, 5, 9, 8, 4])
print reorder([7, 3, 9, 6, 2, 5, 1, 8, 4],5)#,[3, 2, 1, 4, 5, 6, 7, 8, 9])
print reorder([2, 9, 1, 5, 7, 3, 6, 4, 8],5)#,[2, 1, 3, 4, 5, 6, 7, 9, 8])
print reorder([6, 2, 4, 9, 1, 3, 7, 8, 5],5)#,[2, 1, 4, 3, 5, 6, 7, 8, 9])
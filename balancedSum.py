"""
Given an array of numbers, find the pivot, for which the sums of all elements to the left and to the right are equal.
"""
from itertools import accumulate
def balancedSum(arr):
    """
    balancedSum function takes one argument as an array(list)
    """
    #creating a cumulative list (left to right of the Array)
    l=list(accumulate(arr)) 
    
    #creating a cumulative list (Right to left of the Array)
    arr.reverse()
    r=list(accumulate(arr))
    r.reverse()
    
    #find the balance index using for loop
    for i in range(len(arr)):
        if l[i]==r[i]:
            return i

# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def bisection_search(L, e):
    """
    This is to search a value in discrite ones. Alternatively, 'Binary Search'

    inputs:  A list L and a value e to search in the list
    returns: True if you can see e in L or False if you fail.
    """
    low = 0
    high = len(L) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if L[mid] > e:
            high = mid - 1
        elif L[mid] < e:
            low = mid + 1
        else:
            return True
            
    return False
    
    

testList = [1,2,3,5,7,9,18,27]
print(bisection_search(testList, 4))
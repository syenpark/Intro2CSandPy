# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def merge_sort(L):
    """
    """
    if len(L) < 2:
        return L
    
    else:
        mid = len(L)//2
        
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        
        return merge(left, right)
    
def merge(left, right):
    """
    """
    result = []
    
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
            
        else:
            result.append(right[0])
            right = right[1:]
            
    if not left and right:
        result = result + right
        
    if left and not right:
        result = result + left
        
    return result

test = [64, 25, 12, 22, 11]
merge_sort(test)
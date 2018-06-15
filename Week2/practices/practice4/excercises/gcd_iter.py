# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    max_gcd = min(a, b)
    
    if not max_gcd:
        return max(a, b)
    
    for num in range(max_gcd, 1, -1):
        if not (a%num | b%num):
            return num
        
    return 1

print(gcd(12, 9))
         
         
         
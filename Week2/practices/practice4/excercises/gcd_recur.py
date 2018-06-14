# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if not min(a, b):
        return max(a, b)
    
    return gcd(min(a, b), max(a, b)%min(a, b))

print(gcd(12, 17))
         
         
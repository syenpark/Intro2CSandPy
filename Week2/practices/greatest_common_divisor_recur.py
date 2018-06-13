#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:36:01 2018

@author: syenpark
"""
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    smaller = min(a, b)
    bigger = max(a, b)
    
    if smaller == 0:
        return bigger
    else:
        return gcdRecur(smaller, bigger % smaller)

gcdRecur(9, 12)
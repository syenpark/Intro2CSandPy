#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:23:42 2018

@author: syenpark
"""

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = min(a, b)

    for i in range(test, 1, -1):
        if (a%i | b%i) == 0:
            return i
    return 1
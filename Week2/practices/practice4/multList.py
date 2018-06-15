# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def mul_list_recur(l=[0]):
    if len(l) < 2:
        return l[0]
    else:
        return l[0] * mul_list_recur(l[1:])
    
print(mul_list_recur([1,3,5,7,9]))
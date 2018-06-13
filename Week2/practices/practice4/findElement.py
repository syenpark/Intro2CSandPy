# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: syenpark
Python Version: 3.6
"""
def find_elem_recur(e, l):
    if not l:
        return False
    elif len(l) == 1:
        return l[0] == e
    else:
        mid = len(l)//2
        
        return find_elem_recur(e, l[:mid]) | find_elem_recur(e, l[mid:])
    

print(find_elem_recur(1, [1, 2, 3, 5, 7, 8, 9, 15]))
# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def selection_sort(L):
    
    for i in range(0, len(L)-1):
        bigger = i
        
        for j in range(i+1, len(L)):
            if L[bigger] < L[j]:
                bigger = j
        
        if bigger != i:
            L[bigger], L[i] = L[i], L[bigger]
            

test = [64, 25, 12, 22, 11]
selection_sort(test)
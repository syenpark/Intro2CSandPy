# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def selection_sort(L):
    
    for i in range(0, len(L)-1):
        smaller = i
        
        for j in range(i+1, len(L)):
            if L[smaller] > L[j]:
                smaller = j
        
        if smaller != i:
            L[smaller], L[i] = L[i], L[smaller]
            

test = [64, 25, 12, 22, 11]
selection_sort(test)
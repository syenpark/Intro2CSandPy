# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def isPal(x):
    assert type(x) == list
    
    temp = x[:]
    #print(temp, x)
    temp.reverse()
    #print(temp, x)
    return temp == x
    
    
def silly(n):
    result = []
    
    for i in range(n):
        result.append(input('Enter element: '))
    
    if isPal(result):
        print('Yes')
    else:
        print('No')
        

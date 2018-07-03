# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def gen_subsets(items):
    subsets = []
    n = len(items)
    
    for i in range(1 << n):
        temp = []
        
        for j in range(n):
            if (i >> j)%2:
                temp.append(items[j])
                
        subsets.append(temp)
        
    return subsets

test = [1,2,3]
print(gen_subsets(test))


# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def gen_subsets(L):    
    if not L:
        return [[]]
    
    new = []
    extra = L[-1:]
    subsets = gen_subsets(L[:-1])
    
    for subset in subsets:
        new.append(subset + extra)
        
    return subsets + new
     
            
test = [1,2,3,4]
print(gen_subsets(test))
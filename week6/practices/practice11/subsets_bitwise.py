# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""
def gen_subsets(items):
    """
    returns: all subsets
    """
    subsets = []
    n = len(items)
    
    # 1 << n is equal to pow(2, n)
    for i in range(1 << n):
        subset = []
        
        # i >> j is equal to i // pow(2, j)
        # A & 1 is equal to A % 2
        for j in range(n):
            if (i >> j) & 1:
                subset.append(items[j])
                
        subsets.append(subset)
        
    return subsets

test = [1,2,3]
print(gen_subsets(test))


# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
"""
def get_data(aTuple):
    num = ()
    words = ()
    
    for t in aTuple:
        num += (t[0], )
        
        if t[1] not in words:
            words += (t[1], )
            
    small = min(num)
    large = max(num)
    unique = len(words)
    
    return (small, large, unique)


(small, large, words) = get_data(((1, 'mine'), 
                                  (3, 'yours'),
                                  (5, 'ours'),
                                  (7, 'mine')))

print((small, large, words))
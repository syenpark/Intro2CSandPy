# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]], 
           [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
           [['captain', 'america'], [8.0,10.0,96.0]],
           [['deadpool'], []]]

def get_stats(class_list):
    stats = []
    
    for e in class_list:
       stats.append([e[0], e[1], avg(e[1])])
        
    return stats

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0
    


print(get_stats(test_grades))
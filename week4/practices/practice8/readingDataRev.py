# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

data = []

file_name = input('Provide a name of a file of data ')

try:
    fh = open(file_name, 'r')
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            add = new[:-1].split(',')
            data.append(add)
finally:
    fh.close()
    
gradesData = []

if data:
    for student in data:
        try:
            name = student[:-1]
            grades = int(student[-1])
            gradesData.append([name, [grades]])
        except ValueError:
            gradesData.append([student[:], []])
        
        
        
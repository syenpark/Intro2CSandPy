# -*- coding: utf-8 -*-
"""
Spyder Editor

@auther: syenpark
Python Version: 3.6
"""

data = []
file_name = input('Provide a name of a file of data ')

try:
    fh = open(file_name, 'r')
except:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            add_it = new[:-1].split(',')
            data.append(add_it)
finally:
    fh.close()

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 18:33:32 2019

@author: WPZ
"""

# buffer to save content
lines = []
i=0
"""
Make sure that it is in the same working directory with results.txt
"""
with open('results.txt') as f:
    for line in f:
        lines.append(line)
        # remove trivial spaces
        line = line.strip()
        # find year
        if line[0:2] == 'PY':
            year = line[-4:]
            file_to_append = year+'.txt'
            print('year:', line[-4:])
            print('file to append:', file_to_append)
            
        if line=='ER':
            # append to year file
            with open(file_to_append, 'a+') as fw:
                for item in lines:
                    fw.write(item)
            # reset it
            lines = []
            print('file end')
            i=i+1
            print()
print (i)

"""
This program is to re-order the result in the result.txt according to the
year of publishing. It could generate many different small files titled with 
the specific year
"""
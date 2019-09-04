#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:40:34 2019

@author: WPZ"""
#%%

# buffer to save content
lines = []

with open('sample.txt') as f:
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
            print()
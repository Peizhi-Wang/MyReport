# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:41:54 2019

@author: WPZ
"""

"""
Used to collect the Research fields of the publications
"""

SC=[x[3:] for x in open('1945.txt',encoding="UTF-8").readlines() if x.startswith('SC ')]
with open('SC1945.txt','w') as f:
    f.writelines(SC)
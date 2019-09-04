# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:55:12 2019

@author: WPZ
"""
"""
This code is used to detect the language that are being used in the research journals
"""

LA=[x[3:] for x in open('1945.txt',encoding="UTF-8").readlines() if x.startswith('LA ')]
with open('LA1945.txt','w') as f:
    f.writelines(LA)
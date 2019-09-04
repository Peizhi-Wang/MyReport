# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:08:52 2019

@author: WPZ
"""

"""
This code is used to collect the DT that are being used in the research journals
"""
DT=[x[3:] for x in open('1945.txt',encoding="UTF-8").readlines() if x.startswith('DT ')]
with open('DT1945.txt','w',encoding="UTF-8") as f:
    f.writelines(DT)
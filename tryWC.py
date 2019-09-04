# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:12:01 2019

@author: WPZ
"""

"""
This code is used to collect the research topic that are being used in the research journals
"""
WC=[x[3:] for x in open('1945.txt',encoding="UTF-8").readlines() if x.startswith('WC ')]
with open('WC1945.txt','w') as f:
    f.writelines(WC)
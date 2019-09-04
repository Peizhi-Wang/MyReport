# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:01:06 2019

@author: WCH
"""
from collections import Counter

filter_words=["dt","the"," "]
"""
In the new version, you don't need to provide dt because it is deleted in the generating process. But I still include that 
for possible debug use.
"""

def readtxt(file):
    txt=(open(file,"r").read()).lower()
    for ch in filter_words:
        txt=txt.replace(ch,"")
    return txt
txt=(readtxt("DT1970.txt"))
half_result=txt.split("\n")

counter=Counter(half_result)
d=dict(counter)

outfile=open("DT_FrequencyCount1970.txt","w")
outfile.write("Number of Different Publications in All:")
outfile.write("\n")
outfile.write(str(len(dict(counter))))
outfile.write("\n")
outfile.write("Counting Each Publication:")
outfile.write("\n")
for term in d:
    outfile.write(term)
    outfile.write(": ")
    outfile.write(str(d[term]))
    outfile.write("\n")
outfile.close()
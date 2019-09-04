# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:59:12 2019

@author: WPZ
"""

from collections import Counter

filter_words=["la","the"," "]
def readtxt(file):
    txt=open(file,"r").read()
    txt=txt.lower()
    for ch in filter_words:
        txt=txt.replace(ch,"")
    return txt
txt=(readtxt("LA1970.txt"))
half_result=txt.split("\n")
print (half_result)

counter=Counter(half_result)
#print (dict(counter))
#print (type(dict(counter)))
#print (len(dict(counter)))
d=dict(counter)
print (d)

outfile=open("LAresult_FrequencyCount1970.txt","w")
outfile.write("Number of Different Languages in All:")
outfile.write("\n")
outfile.write(str(len(dict(counter))))
outfile.write("\n")
outfile.write("Counting Each Language:")
outfile.write("\n")
for term in d:
    outfile.write(term)
    outfile.write(": ")
    outfile.write(str(d[term]))
    outfile.write("\n")
outfile.close()
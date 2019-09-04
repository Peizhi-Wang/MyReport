# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:13:13 2019

@author: WCH
"""

from collections import Counter

filter_words=["wc"," "]
def readtxt(file):
    txt=open(file,"r").read()
    txt=txt.lower()
    for ch in filter_words:
        txt=txt.replace(ch,"")
    return txt
txt=(readtxt("WC1970.txt"))
#print (txt)
half_result=txt.split("\n")
#print (half_result)

final_result=[]
for term in half_result:
    lems=term.split(";")
    for term in lems:
        final_result.append(str(term))
#print (final_result)


counter=Counter(final_result)
#print (dict(counter))
#print (type(dict(counter)))
#print (len(dict(counter)))
d=dict(counter)
#print (d)
d_order=sorted(d.items(),key=lambda x:x[1],reverse=True) 
#print (d_order)
print (counter.most_common(10))

outfile=open("WCresult_FrequencyCount1970.txt","w")
outfile.write("Number of Different Research Topics in All:")
outfile.write("\n")
outfile.write(str(len(d_order)))
outfile.write("\n")
outfile.write("Counting Each Research Topics:")
outfile.write("\n")
for term in d_order:
    outfile.write(str(term))
    #outfile.write(": ")
    #outfile.write(str(d[term]))
    outfile.write("\n")
outfile.close()  
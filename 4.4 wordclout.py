# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:30:33 2019

@author: WPZ
"""
"""
This is the program to generate word-cloud
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

f = open('C:/Users/WCH/Desktop/1945 txt/SC1945.txt','r').read()
wordcloud = WordCloud(background_color="white",width=1000,height=860,margin=2,collocations=False).generate(f)
plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")
plt.show()
wordcloud.to_file('C:/Users/WCH/Desktop/1945 txt/1945PIC/1945SC.png')
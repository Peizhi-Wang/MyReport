# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:02:01 2019

@author: WPZ
"""
import numpy as np
import pandas as pd
import gensim
import nltk
from nltk.tokenize import RegexpTokenizer as RT
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models

# Create a tokenizer here first 
tokenizer = RT(r'\w+')
 
# For here, generating the stopword list for English. We also need to include
# some extra words
en_stop = get_stop_words('en')
en_stop.append("ti")
#print (en_stop)

#de_stop=get_stop_words("de")
#print (de_stop)
 
# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents. We just don't need to use that. That is just for testing
"""
doc_a=A public/private benefits framework for the design of polices oriented
doc_b=Climate vulnerability and contrasting climate perceptions as an element
doc_c=Agro-pastoralism under climate change: Institutions and local climate
doc_d=Carbon stocks and biodiversity conservation on a small island: Pico (the
doc_e=A grassland strategy for farming systems in Europe to mitigate GHG
"""
 
# compile sample documents into a list
#doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]
#print (doc_set)

with open("C:/Users/WCH/Desktop/2017 Title/Title2017.txt") as f:
  #print (f.readlines())
  #print (f.readlines())
  doc_set=f.readlines()
 
#Creating a new list for tokenized documents
texts = []
 
for docu in doc_set:
    tokens = tokenizer.tokenize(docu.lower())
    stopped_tokens=[]
    for i in tokens:
        if i not in en_stop:
            stopped_tokens.append(i)    
    stemmed_tokens=[]
    for i in stopped_tokens:
        stemmed_tokens.append(p_stemmer.stem(i))
    texts.append(stemmed_tokens)
dictionary = corpora.Dictionary(texts)
corpus=[]
for text in texts:
    corpus.append(dictionary.doc2bow(text))
 
# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=1, id2word = dictionary, passes=20)
print(ldamodel.print_topics(num_topics=1, num_words=30))
"""
Setting the parameters that you want! Then enjoy that! See, it is flying
"""

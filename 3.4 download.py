# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:39:55 2019

@author: WPZ
"""

import urllib2
data = (urllib2.urlopen("The link to the online txt file")).read()

# Write data to file
fileN = open("result.txt", 'w')
fileN.write(data)
fileN.close()

"""
In practice, I strongly recommend you not use this program as the size of the 
program is too large. You could consider about other tools like IDM etc.
"""
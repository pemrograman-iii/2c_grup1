# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:36:45 2019

@author: PandA23
"""

from matplotlib import pyplot as ariq

print(1174087%3+2)

def ariq_scatter():
    x = [1,4,5,7,23]
    y = [13,21,55,62,101]

    x1 = [12,14,15,8,30]
    y1 = [4,6,5,7,2]

    x2 = [22,24,55,70,40]
    y2 = [10,21,90,30,90]

    ariq.subplot(221)
    ariq.scatter(x,y)
    ariq.subplot(222)
    ariq.scatter(x1,y1)
    ariq.subplot(223)
    ariq.scatter(x2,y2)
    ariq.show() 
    
ariq_scatter()  
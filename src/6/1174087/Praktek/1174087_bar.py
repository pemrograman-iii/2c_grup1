# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:36:06 2019

@author: PandA23
"""

from matplotlib import pyplot as ariq

print(1174087%3+2)

def bar_ariq():
    x = [1,3,5,7,9,11]
    y = [20,40,60,80,100,120]

    x1 = [2,4,18,29,11]
    y1 = [4,9,13,7,6]

    x2 = [20,60,80,30,40,20,10]
    y2 = [10,50,10,50,10,50,10]

    ariq.subplot(221)
    ariq.bar(x,y)
    ariq.subplot(222)
    ariq.bar(x1,y1)
    ariq.subplot(223)
    ariq.bar(x2,y2)
    ariq.show() 

bar_ariq()
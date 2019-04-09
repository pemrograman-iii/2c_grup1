# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:38:18 2019

@author: PandA23
"""

from matplotlib import pyplot as ariq

print(1174087%3+2)

def ariq_plot():
    x = [2,4,6,8,10]
    y = [15,30,45,60,90]

    x1 = [1,2,3,4,5]
    y1 = [6,7,8,9,10]

    x2 = [71,61,51,41,31]
    y2 = [11,21,31,41,51]

    ariq.subplot(221)
    ariq.plot(x,y)
    ariq.subplot(222)
    ariq.plot(x1,y1)
    ariq.subplot(223)
    ariq.plot(x2,y2)
    ariq.show()
    
ariq_plot()
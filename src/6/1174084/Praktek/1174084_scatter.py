# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:02:56 2019

@author: Reza
"""

from matplotlib import pyplot as pyp

print(1174084%3+2)

def scatter():
    x = [18,13,9,7,9,11,4]
    y = [10,12,6,19,23,24,11]
    x1 = [4,8,13,14,3]
    y1 = [6,7,1,8,11]
    x2 = [2,5,6,10,8,4,20]

    pyp.subplot(311)
    pyp.scatter(x,y)
    pyp.subplot(312)
    pyp.scatter(x1,y1)
    pyp.subplot(313)
    pyp.scatter(x,x2)
    pyp.show()

    
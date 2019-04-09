# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:05:44 2019

Chapter 6 Praktikum

@author: Bakti Qilan
"""
from matplotlib import pyplot as plot
import numpy as np
def bar(b):
    if b == 4:
        x = [2,5,6,2,8]
        y = [1,3,7,8,9]     
        x1 = [10,23,22,11,25,22,17,12,15,18]
        y1 = [23,22,25,24,21,22,26,29,11,16]
        x2 = [1,2,3,4,5,6,7,8,9,10]
        y2 = [11,12,13,14,15,16,17,18,19,20]
        x3 = [2,4,6,8,10,12]
        y3 = [3,5,7,9,11,13]
        plot.subplot(221)
        plot.bar(x,y)
        plot.subplot(222)
        plot.bar(x1,y1)
        plot.subplot(223)
        plot.bar(x2,y2)
        plot.subplot(224)
        plot.bar(x3,y3)
        plot.show()
    elif b == 3:
        x = [1,2,3,4,5]
        y = [2,3,6,5,7]     
        x1 = [10,23,22,11,25,22,17,12,15,18]
        y1 = [23,22,25,24,21,22,26,29,11,16]
        x2 = [1,2,3,4,5,6,7,8,9,10]
        y2 = [11,12,13,14,15,16,17,18,19,20]
        plot.subplot(221)
        plot.bar(x,y)
        plot.subplot(222)
        plot.bar(x1,y1)
        plot.subplot(223)
        plot.bar(x2,y2)
        plot.show()
    elif b == 2:
        x = np.random.randint(0, 10, 10)
        y = np.random.randint(0, 10, 10)
        x1 = np.random.randint(10, 20, 10)
        y1 = np.random.randint(10, 20, 10)
        plot.subplot(211)
        plot.bar(x,y)
        plot.subplot(212)
        plot.bar(x1,y1)
        plot.show()
    elif b == 1:
        x = np.random.randint(0, 10, 10)
        y = np.random.randint(0, 10, 10)
        x1 = np.random.randint(10, 20, 10)
        y1 = np.random.randint(10, 20, 10)
        plot.subplot(111)
        plot.bar(x,y)
        plot.show()
    else:
        print("Data tidak Valid")
        
        
npm = input("Masukkan NPM Anda: ")
modnpm = int(npm)%3+2
print(modnpm)

if modnpm == 4:
    bar(4)
elif modnpm == 3:
    bar(3)
elif modnpm == 2:
    bar(2)
elif modnpm == 1:
    bar(1)
else:
    print("Data tidak Valid")
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:43:23 2019

@author: Aspire E15
"""
# No 1
from matplotlib import pyplot as plt
import numpy as np
def bar(mod):
    if mod == 3:
        x = [1,2,3,4,5]
        y = [2,3,6,5,7]     
        x1 = [10,23,22,11,25,22,17,12,15,18]
        y1 = [23,22,25,24,21,22,26,29,11,16]
        x2 = [1,2,3,4,5,6,7,8,9,10]
        y2 = [11,12,13,14,15,16,17,18,19,20]
        plt.subplot(221)
        plt.bar(x,y)
        plt.subplot(222)
        plt.bar(x1,y1)
        plt.subplot(223)
        plt.bar(x2,y2)
        plt.show()
    elif mod == 2:
        x = np.random.randint(0, 10, 10)
        y = np.random.randint(0, 10, 10)
        x1 = np.random.randint(10, 20, 10)
        y1 = np.random.randint(10, 20, 10)
        plt.subplot(211)
        plt.bar(x,y)
        plt.subplot(212)
        plt.bar(x1,y1)
        plt.show()
    elif mod == 1:
        x = np.random.randint(0, 10, 10)
        y = np.random.randint(0, 10, 10)
        x1 = np.random.randint(10, 20, 10)
        y1 = np.random.randint(10, 20, 10)
        plt.subplot(111)
        plt.bar(x,y)
        plt.show()
    else:
        print("Data tidak Valid")
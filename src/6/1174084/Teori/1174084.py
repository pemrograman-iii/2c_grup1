# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:58:04 2019

@author: Reza
"""

from matplotlib import pyplot as pyp

x = [2,4,3]
y = [4,2,1]

pyp.plot(x,y)
pyp.show()
#%%
from matplotlib import pyplot as pyp

x=[1,3,5,7,9]
y=[35,60,20,25,70]
pyp.bar(x,y, label="Toyota",color='Y',width=.5)
pyp.legend()
pyp.xlabel('Days')
pyp.ylabel('Distance (kms)')
pyp.title('Information')
pyp.show()
#%%
from matplotlib import pyplot as pyp

x = [2,4,6,5,42,54,3,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,34,24,43,54,33,2,44,4,24,76,32,23,23,32,24,2,1,54,76,53,54]
y = [0,20,40,60,80,100]
pyp.hist(x, y, histtype='bar', rwidth=0.9)
pyp.xlabel('age groups')
pyp.ylabel('Number of people')
pyp.title('Histogram')
pyp.show()
#%%
from matplotlib import pyplot as pyp

x = [2,1.5,1,2.5,3,7.5,4.1]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
pyp.scatter(x,y, label='Pendapatan Tinggi Tapi Penyimpanan Rendah',color='R')
pyp.xlabel('Pensimpanan dalam ratusan')
pyp.ylabel('Pendapatan dalam ribuan')
pyp.title('Diagram Titik')
pyp.legend()
pyp.show()
#%%
from matplotlib import pyplot as pyp

x = [5,2,1,7]
y = [6,8,2,9]
x1 = [4,1,6,8]
y1 = [9,6,3,9]
pyp.subplot(331)
pyp.plot(x, y)
pyp.subplot(332)
pyp.plot(x1, y1)
pyp.subplot(333)
pyp.bar(x, y)
pyp.subplot(334)
pyp.bar(x1, y1)
pyp.subplot(335)
pyp.hist(x, 5)
pyp.subplot(336)
pyp.hist(x, 4)
pyp.subplot(337)
pyp.scatter(x, y)
pyp.subplot(338)
pyp.scatter(x1, y1)
pyp.subplot(339)
pyp.scatter(x1, y)
pyp.show()
#%%

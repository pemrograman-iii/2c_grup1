# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:27:18 2019

@author: PandA23
"""
#%% plot
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [12, 24, 14, 8]
plt.plot(x, y)
plt.show()

#%% bar
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [12, 24, 14, 8]
plt.bar(x, y)
plt.show()

#%% histrogram
import matplotlib.pyplot as plt
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
plt.hist(x, 3)
plt.show()

#%% Scatter 
import matplotlib.pyplot as plt
x = [2,4,6,7,9,13,19]
y = [54,72,43,2,8,98,76]
x1 = [1,6,14,19,25,29,30]
y2 = [24,35,23,5,8,7,19]
plt.scatter(x,y, label='Angka 1',color='R')
plt.scatter(x1,y2, label='Angka 2',color='B')
plt.xlabel('Random 1')
plt.ylabel('Random 2')
plt.title('Diagram Titik')
plt.legend()
plt.show()

#%% Subplot
x = [1,2,3,4,5]
y = [6,7,8,9,10]
plt.subplot(331)#(tinggi,lebar,urutan)
plt.plot(x, y)
plt.subplot(332)
plt.bar(x, y)
plt.subplot(333)
plt.hist(x, 2)
plt.subplot(334)
plt.plot(x, y)
plt.subplot(335)
plt.plot(x, y)
plt.subplot(336)
plt.scatter(x, y)
plt.subplot(337)
plt.scatter(x, y)
plt.subplot(338)
plt.bar(x, y)
plt.subplot(339)
plt.hist(x, 2)
plt.show()


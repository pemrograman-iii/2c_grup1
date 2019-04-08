# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:11:41 2019

Teori Chapter 6 matplotlib

@author: Bakti Qilan
"""

#%% No.1
from matplotlib import pyplot as plot

x=[1,3,5]
y=[2,4,6]

plot.plot(x,y)
plot.xlabel('x')
plot.ylabel('y')
plot.show

#%% No.2

x=[1,2,4]
y=[1,4,4]
a=[1,3,5]
b=[1,5,6]

plot.plot(x,y,a,b)
plot.xlabel('x')
plot.ylabel('y')
plot.show

#%% No.3

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plot.scatter(x,y, label='data', color='k', s=25, marker="o")

plot.xlabel('x')
plot.ylabel('y')
plot.legend()
plot.show()

#%%
rentang_umur = [40,80,11,22,16,9,10,15,22,55,62,45,21,22,102,
                95,85,55,110,120,70,80,75,65,54,39,32,41,46,44]
bins = [0,10,20,30,40,50,60,70,80,90,100]

plot.hist(rentang_umur, bins, histtype='bar', rwidth=0.8)
plot.xlabel('Umur')
plot.ylabel('Jumlah Orang')
plot.show()

#%%
import numpy as np

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
 
plot.barh(y_pos, performance, align='center', alpha=0.5)
plot.yticks(y_pos, objects)
plot.xlabel('Pemakai')
plot.title('Penggunaan bahasa Pemrograman')
plot.show()

#%%
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]
plot.subplot(331).set_title('1')#tinggi,lebar,urutan
plot.plot(x, y)
plot.subplot(333).set_title('3')
plot.bar(x, y)
plot.subplot(334).set_title('4')
plot.hist(x, y)
plot.subplot(335).set_title('5')
plot.scatter(x, y)
plot.subplot(339).set_title('9')
plot.barh(x, y)
plot.show()

#%% color_plot
from __future__ import division

import matplotlib.pyplot as plt
from matplotlib import colors as mcolors


colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

# Sort colors by hue, saturation, value and name.
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]

n = len(sorted_names)
ncols = 4
nrows = n // ncols + 1

fig, ax = plt.subplots(figsize=(8, 5))

# Get height and width
X, Y = fig.get_dpi() * fig.get_size_inches()
h = Y / (nrows + 1)
w = X / ncols

for i, name in enumerate(sorted_names):
    col = i % ncols
    row = i // ncols
    y = Y - (row * h) - h

    xi_line = w * (col + 0.05)
    xf_line = w * (col + 0.25)
    xi_text = w * (col + 0.3)

    ax.text(xi_text, y, name, fontsize=(h * 0.8),
            horizontalalignment='left',
            verticalalignment='center')

    ax.hlines(y + h * 0.1, xi_line, xf_line,
              color=colors[name], linewidth=(h * 0.6))

ax.set_xlim(0, X)
ax.set_ylim(0, Y)
ax.set_axis_off()

fig.subplots_adjust(left=0, right=1,
                    top=1, bottom=0,
                    hspace=0, wspace=0)
plt.show()

#%%
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
plot.hist(x, 10,  histtype ='bar' , rwidth =0.9)
plot.xlabel('Angka')
plot.ylabel('Banyaknya angka rentang dari 10')
plot.show()
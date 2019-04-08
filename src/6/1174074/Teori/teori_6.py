# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:48:59 2019

@author: Aspire E15
"""
#no 2
import matplotlib.pyplot as plt
x = [2,4,6,8]
y = [3,6,9,11]
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu y')
plt.scatter(x,y)
plt.show()
#%%
#no 3
#Plot Line
import matplotlib.pyplot as plt
x = (4,8,13,17,20)
y = (54, 67, 98, 78, 45)
plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45])
plt.show()
#%%
#Plot Bar
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = ('Lari', 'Lompat', 'Renag', 'Panahan', 'Lempar', 'Jalan')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
 
plt.bar(y_pos, performance, align='center', alpha=0.8)
plt.xticks(y_pos, objects)
plt.ylabel('Banyak Atlit')
plt.title('Cabang Olahraga')
plt.show()
#%%
#Plot Histogram
import matplotlib.pyplot as plt
x = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
num_bins = 6
n, bins, patches = plt.hist(x, num_bins, facecolor = 'g')
plt.show()
#%%
#Plot Scatter
import matplotlib.pyplot as plt
x = [1,3,5,7]
y = [2,4,6,8]
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu y')
plt.scatter(x,y, facecolor = 'g')
plt.show()
#%%
#Stack Plot
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 1, 2, 3, 5]
y2 = [0, 4, 2, 6, 8]
y3 = [1, 3, 5, 7, 9]

y = np.vstack([y1, y2, y3])

fig, ax = plt.subplots()
ax.stackplot(x, y)
plt.show()
#%%
#no 4
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 1, 2, 3, 5]
y2 = [0, 4, 2, 6, 8]
y3 = [1, 3, 5, 7, 9]

y = np.vstack([y1, y2, y3])

labels = ["Honda", "Yamaha", "Suzuki"]#codingan Label

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3, labels=labels)
ax.legend(loc='upper left')#codingan legend
plt.show()
#%%
#no 5
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.subplot(931)
plt.plot(t1, f(t1), t2, f(t2))

plt.subplot(932)
plt.plot(t2, np.cos(2*np.pi*t2))

plt.subplot(933)
plt.plot(t1, f(t1), t2, f(t2))

plt.subplot(934)
plt.plot(t2, np.cos(2*np.pi*t2))

plt.subplot(935)
plt.plot(t1, f(t1), t2, f(t2))

plt.subplot(936)
plt.plot(t2, np.cos(2*np.pi*t2))

plt.subplot(937)
plt.plot(t1, f(t1), t2, f(t2))

plt.subplot(938)
plt.plot(t2, np.cos(2*np.pi*t2))

plt.subplot(939)
plt.plot(t1, f(t1), t2, f(t2))
plt.show()
#%%
#no 7
import matplotlib.pyplot as plt
x = [2,4,6,5,42,543,5,3,73,64,42,97,63,76,63,8,73,97,23,45,56,89,45,3,23,2,5,78,23,56,67,78,8,3,78,34,67,23,324,234,43,544,54,33,223,443,444,234,76,432,233,23,232,243,222,221,254,222,276,300,353,354,387,364,309]
num_bins = 6
n, bins, patches = plt.hist(x, num_bins, facecolor = 'b')
plt.show()
#%%
#no 8
import matplotlib.pyplot as plt

labels = 'Mengoding', 'Membaca', 'Menonton', 'Mancing'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

plt.show()

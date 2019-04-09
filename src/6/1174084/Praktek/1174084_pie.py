# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:55:44 2019

@author: Reza
"""

from matplotlib import pyplot as pyp

print(1174084%3+2)

def pie(): 
    data1 = [5,2,10,3]
    data2 = [3,7,5,5]
    data3 = [9,2,9,17]
    olahraga = ['Basket','Bulutangkis','Futsal','Sepakbola']
    pelajaran = ['IPA','IPS','MTK','KIMIA']
    cols = ['r','b','c','y']

    pyp.subplot(131)
    pyp.pie(data1,
             labels=olahraga,
             colors=cols,
             startangle=0,
             shadow= True,
             explode=(0,0,0.2,0),
             autopct='%1.1f%%')
    pyp.title('Pie Chart Data 1')

    pyp.subplot(132)
    pyp.pie(data2,
             labels=pelajaran,
             colors=cols,
             startangle=90,
             shadow=True,
             explode=(0,0.2,0,0),
             autopct='%1.1f%%')
    pyp.title('Pie Chart Data 2')

    pyp.subplot(133)
    pyp.pie(data3,
             labels=olahraga,
             colors=cols,
             startangle=90,
             shadow=True,
             explode=(0,0,0,0.2),
             autopct='%1.1f%%')
    pyp.title('Pie Chart Data 3')
    pyp.show()

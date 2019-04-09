# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:07:47 2019

Chapter 6 Praktikum

@author: Bakti Qilan
"""
from matplotlib import pyplot as plt

def pie(mod):
    if mod == 2:
        merk= [5,10,2,3]
        prog = [7,5,6,1]
        jns_merk = ['Acer','Asus','Lenovo','HP']
        programming = ['Perl','Java','C++','Python']
        cols = ['silver','lime','gold','aqua']
        plt.subplot(121)
        plt.pie(merk,
                 labels=jns_merk,
                 colors=cols,
                 startangle=0,
                 shadow= True,
                 explode=(0.2,0,0,0),
                 autopct='%1.1f%%')
        plt.title('Pie Laptop')
                
        plt.subplot(122)
        plt.pie(prog,
                 labels=programming,
                 colors=cols,
                 startangle=90,
                 shadow=True,
                 explode=(.1,0,0,0),
                 autopct='%1.1f%%')
        plt.title('Pie Programming')
        plt.show()
    else:
        print("Data tidak ada")

npm = input("Masukkan NPM Anda: ")
modnpm = int(npm)%3+2
print(modnpm)

if modnpm == 4:
    print("Data tidak ada")
elif modnpm == 3:
    print("Data tidak ada")
elif modnpm == 2:
    pie(2)
elif modnpm == 1:
    print("Data tidak ada")
else:
    print("Data tidak Valid")
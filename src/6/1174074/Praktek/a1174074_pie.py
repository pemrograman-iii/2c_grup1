# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:03:36 2019

@author: Aspire E15
"""

#No 3
from matplotlib import pyplot as plt

def pie(mod):
    if mod == 3:
        Jobs = [8,1,14,2]
        movie = [10,18,4]
        sport = [7,5,6,1]
        Profesi = ['Programmer','Atlit','Gamer','Youtuber']
        Film = ['Avengers','John Wick','Shazam']
        Olahraga = ['Basket','Futsal','Voli','Baseball']
        cols = ['m','r','c','b']
        plt.subplot(221)
        plt.pie(Jobs,
                 labels=Profesi,
                 colors=cols,
                 startangle=0,
                 shadow= True,
                 explode=(0.2,0,0,0),
                 autopct='%1.1f%%')
        plt.title('Pie Profesi')
        
        plt.subplot(222)
        plt.pie(movie,
                 labels=Film,
                 colors=cols,
                 startangle=90,
                 shadow=True,
                 explode=(.3,0.1,0),
                 autopct='%1.1f%%')
        plt.title('Pie Movie')
        
        plt.subplot(223)
        plt.pie(sport,
                 labels=Olahraga,
                 colors=cols,
                 startangle=90,
                 shadow=True,
                 explode=(.1,0,0,0),
                 autopct='%1.1f%%')
        plt.title('Pie Olahraga')
        plt.show()
    else:
        print("Data belum dimasukkan")

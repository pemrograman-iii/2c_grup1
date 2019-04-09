# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:37:36 2019

@author: PandA23
"""

from matplotlib import pyplot as ariq

print(1174087%3+2)

def ariq_pie(): 
    hobi = [1,2,3]
    game = [1,50,30]
    wisata = [1,4,5]
    Hobbies = ['Tidur','Makan','Game']
    Games = ['Builder','Survival','Action']
    Tourism = ['Pantai','Gunung','Air Terjun']
    cols = ['c','r','m']

    ariq.subplot(221)
    ariq.pie(hobi,
             labels=Hobbies,
             colors=cols,
             startangle=0,
             shadow= True,
             explode=(0.1,0.1,0.1),
             autopct='%1.1f%%')
    ariq.title('Hobi Ariq')

    ariq.subplot(222)
    ariq.pie(game,
             labels=Games,
             colors=cols,
             startangle=90,
             shadow=True,
             explode=(0.2,0.1,0),
             autopct='%1.1f%%')
    ariq.title('Game Ariq')

    ariq.subplot(223)
    ariq.pie(wisata,
             labels=Tourism,
             colors=cols,
             startangle=0,
             shadow=True,
             explode=(0.1,0,0),
             autopct='%1.1f%%')
    ariq.title('Wisata Ariq')
    ariq.show() 

ariq_pie()
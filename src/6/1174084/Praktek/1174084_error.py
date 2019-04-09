# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:45:16 2019

@author: Reza
"""

from matplotlib import pyplot as pyp

x = [18,13,9,7,9,11,4]
y = [10,12,6,19,23,24,11]
x1 = [4,8,13,14,3]
y1 = [6,7,1,8,11]
x2 = [2,5,6,10,8,4,20]
        
def tryExceptError():
    try: 
        pyp.plot(x1,x2)  
        pyp.show()  
    except ValueError:
        print("Nilai yang dimasukan ada masalah")
    except NameError:
        print("Variable yang dicari tidak ada")
    except SyntaxError:
        print("Penulisan syntax ada masalah!")   
    except:
        print("Sepertinya ada sedikit masalah!")

tryExceptError()
#%%

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:13:56 2019

Chapter 6 Praktikum

@author: Bakti Qilan
"""
from matplotlib import pyplot as plot

def PenangananError():
    try:
        a=[1,2,3]
        b=[5,2,4]        
        plot.plot(a,b)        
        plot.show()        
    except SyntaxError:
        print("Kesalahan pada penulisan syntax")
    except NameError:
        print("Variable yang anda maksud tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi error")
        
PenangananError()
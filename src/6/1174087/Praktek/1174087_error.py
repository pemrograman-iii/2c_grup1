# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:38:59 2019

@author: PandA23
"""

def ariq_error():
    try:
        from matplotli import pyplot as plt
    except SyntaxError:
        print("Ada kesalahan dalam penulisan Syntax")
    except NameError:
        print("Variable yang dimasukkan tidak ada")
    except TypeError:
        print("Ada yang salah pada type data")
    except:
        print("Sedang terjadi sebuah kesalahan")

ariq_error() 
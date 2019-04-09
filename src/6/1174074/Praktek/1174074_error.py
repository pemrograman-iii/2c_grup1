# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:19:16 2019

@author: Aspire E15
"""
def PenangananError():
    try:
        from matplotlib import pyplot as plt
    except SyntaxError:
        print("Ada kesalahan dalam penulisan Code")
    except NameError:
        print("Variable yang dimasukkan tidak ada")
    except TypeError:
        print("Ada yang salah pada type data")
    except:
        print("Terjadi kesalahan")

PenangananError()

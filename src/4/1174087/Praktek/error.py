# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:59:01 2019

@author: PandA23
"""
import pandas

def errorpandas():
    try:
        df = pandas.read_csv('databaca.csv')
        print(dt)
    except NameError:
        print("Variable Tidak tepat")

errorpandas() 
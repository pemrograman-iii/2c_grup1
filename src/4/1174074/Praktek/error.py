# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 00:19:57 2019

@author: Aspire E15
"""

import pandas

def errorpandas():
    try:
        dt = pandas.read_csv('hasil1.csv')
        print(df)
    except NameError:
        print("Variable kurang tepat")

errorpandas() 
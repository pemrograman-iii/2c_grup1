# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:18:14 2019

@author: PandA23
"""
import pandas

def modelistpandas():
    df = pandas.read_csv('databaca.csv')
    print(df)
    
def modedicpandas():
   df = pandas.read_csv('databaca.csv')
   data = pandas.DataFrame.from_dict(df)
   print(data)
   
def menulispandas():
    data = {'Nama': ['Ilham Muhammad Ariq'],
            'Kelas': ['D4TI2C']}
    df= pandas.DataFrame.from_dict(data)
    df.to_csv('datatulis_pandas.csv')
    print(df)   

def merubahformattanggal():
    df = pandas.read_csv('databaca.csv',parse_dates=['tanggal lahir'])
    print(df)
    
def merubahindexkolom():
    df = pandas.read_csv('databaca.csv')
    df.index = ['No-1','No-2']
    print(df)
    
def merubahnamakolom():
    df = pandas.read_csv('databaca.csv')    
    df.columns = ['npm','nama lengkap','tanggal lahir']
    print(df)
    
    
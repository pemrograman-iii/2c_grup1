# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:43:00 2019

@author: Aspire E15
"""
import pandas

def modelistpandas():
    df = pandas.read_csv('hasil1.csv')
    print(df)
    
def modedicpandas():
   df = pandas.read_csv('hasil1.csv')
   data = pandas.DataFrame.from_dict(df)
   print(data)
   
def menulispandas():
    data = {'Nama': ['M.Arifqi.R'],
            'Kelas': ['D4TI2C']}
    df= pandas.DataFrame.from_dict(data)
    df.to_csv('hasil5.csv')
    print(df)   

def merubahformattanggal():
    df = pandas.read_csv('hasil1.csv',parse_dates=['tanggal lahir'])
    print(df)
    
def merubahindexkolom():
    df = pandas.read_csv('hasil1.csv')
    df.index = ['No-1','No-2']
    print(df)
    
def merubahnamakolom():
    df = pandas.read_csv('hasil1.csv')    
    df.columns = ['nama','npm','tanggal lahir']
    print(df)
    
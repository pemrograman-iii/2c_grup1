# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:59:03 2019

Chapter 4.2

@author: Bakti Qilan
"""
import pandas

#No. 3
def membukaPandasModeList():
    pr = pandas.read_csv('no.1.csv')
    print(pr)

#No. 4
def membukaPandasModeDict():
    pr = pandas.read_csv('no.1.csv')
    pd = pandas.DataFrame.from_dict(pr)
    print(pd)
    
#No. 5
def merubahFormatTanggal():
    prd = pandas.read_csv('no.1.csv', parse_dates=['tanggal lahir'])
    print(prd)
    
#No. 6
def merubahIndexKolom():
    pri = pandas.read_csv('no.1.csv')
    pri.index = ['ke-1', 'ke-2', 'ke-3']
    print(pri)
    
#No.7
def merubahNamaKolom():
    df = pandas.read_csv('no.1.csv')
    df.columns =['kolom1', 'kolom2', 'kolom3', 'kolom4', 'kolom5'] 
    print(df)
    
#membuatcsvPandas
def membuatCSVPandas():
    df = pandas.read_csv('no.1.csv', 
         index_col='NPM', 
         parse_dates=['Tanggal Lahir'],
         header=0, 
         names=['NPM', 'Nama', 'Kelas','Golongan Darah', 'Tanggal Lahir'])
    df.to_csv('membuatCSVPandas.csv')
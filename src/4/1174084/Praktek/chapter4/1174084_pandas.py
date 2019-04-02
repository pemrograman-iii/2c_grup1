# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:56:44 2019

@author: Reza
"""

import pandas

#No. 3
def membukaListPandas():
    df = pandas.read_csv('data1.csv')
    print(df)


#No. 4
def membukaDictPandas():
    df = pandas.read_csv('data1.csv')
    dt = pandas.DataFrame(df)
    print(dt['nama'])
 
    
#No. 5
def mengubahFormatTanggal():
    df = pandas.read_csv('data1.csv', parse_dates=['tanggal lahir'])
    print(df)
    

#No. 6
def mengubahIndexKolom():
    df = pandas.read_csv('data1.csv')
    df.index = ['1', '2']
    print(df)
    

#No. 7
def mengubahNamaKolom():
    df = pandas.read_csv('data1.csv')
    df.columns =['NAMA', 'NPM', 'KELAS', 'TANGGAL LAHIR'] 
    print(df)
    

#Membuat
def membuatPandas():
    df = pandas.read_csv('data1.csv', 
            index_col='Nama', 
            parse_dates=['Tanggal Lahir'],
            header=0, 
            names=['Nama', 'NPM', 'Kelas', 'Tanggal Lahir'])
    df.to_csv('data2.csv')
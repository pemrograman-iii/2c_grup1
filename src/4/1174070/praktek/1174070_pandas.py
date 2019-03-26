# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 00:28:55 2019

@author: User
"""
import pandas
#no3
df = pandas.read_csv('isi.csv')
print(df)

#no4
df = pandas.read_csv('isi.csv')
uji = pandas.DataFrame.from_dict(df)
print(uji)

#no5
df = pandas.read_csv('isi.csv', parse_dates=['Hire Date'])
print(df)

#no6
df = pandas.read_csv('isi.csv', index_col='Name')
print(df)

#no7
df = pandas.read_csv('isi.csv',
        header=0, 
        names=['Nama', 'Tgl Masuk','Gaji', 'Jatah Sakit'])
print(df)

def bacalistpandas():
    df = pandas.read_csv('isi.csv')
    print(df)

def write():
    df = pandas.read_csv('isi.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])

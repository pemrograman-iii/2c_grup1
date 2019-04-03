# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:21:25 2019

Chapteer 5 Praktek M Arifqi R

@author: Aspire E15
"""
import csv
   
def baca(NamaFile):
    with open(NamaFile, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['Ready'])
            
baca("1174074.csv")
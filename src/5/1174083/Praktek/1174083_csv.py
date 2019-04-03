# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:00:29 2019

Chapter 5 Praktek

@author: Bakti Qilan
"""

import csv
   
def baca(NamaFile):
    with open(NamaFile, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['Ready'])
            
baca("1174083.csv")
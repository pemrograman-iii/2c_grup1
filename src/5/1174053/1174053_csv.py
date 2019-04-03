# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:29:21 2019

@author: ASUS
"""

import csv

def becacsv():
    with open('uji.csv',mode='r') as csv_file:
        baca = csv.DictReader(csv_file)
        for row in baca:
            print(row['jarak'])
            
becacsv()
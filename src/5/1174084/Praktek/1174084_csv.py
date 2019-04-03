# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:30:12 2019

@author: Reza
"""

import csv
   
def read(namafile):
    with open(namafile, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['Ready'])
            
read("1174084.csv")
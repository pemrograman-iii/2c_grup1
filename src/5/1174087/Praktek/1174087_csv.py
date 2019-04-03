# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:48:41 2019

@author: PandA23
"""

import csv

def bacaCsv():
    with open('1174087.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['jarak'])
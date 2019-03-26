# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:20:05 2019

@author: Bakti Qilan
"""
import csv

with open('no.1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2], row[3], row[4])

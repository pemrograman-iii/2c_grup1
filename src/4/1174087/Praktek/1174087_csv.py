# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:14:27 2019

@author: PandA23
"""

import csv

def modelistcsv():
    with open('databaca.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])
            
def modediccsv():
    with open('databaca.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['tanggal lahir'])

def menuliscsv():
    data = {
    ('Ariq', 'D4TI2C', 100),
    ('Reza','D4TI2C',90)
    }
    data_file = open('datatulis_csv.csv', 'w')
    w = csv.writer(data_file)
    w.writerow(('Nama','Kelas','Nilai'))
    for s in data:
        w.writerow(s)


    
    
           
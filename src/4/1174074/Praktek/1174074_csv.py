# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:11:10 2019

@author: Aspire E15
"""

import csv

def modelistcsv():
    with open('hasil1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2], row[3])
            
def modediccsv():
    with open('hasil1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['nama'], row['npm'], row['kelas'], row['tanggal lahir'])

def menuliscsv():
    data = {
    ('Ramadhan', '1174072', 'D4TI2C'),
    ('Ade','1174073','D4TI2C')
    }
    data_file = open('hasil3.csv', 'w')
    w = csv.writer(data_file)
    w.writerow(('nama','npm','kelas'))
    for s in data:
        w.writerow(s)
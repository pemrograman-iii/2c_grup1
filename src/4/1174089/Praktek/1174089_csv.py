# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:38:47 2019

@author: ADVENT
"""

import csv

#Jawaban No. 1
def bukaModeListCsv():
    with open('teori.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2], row[3])

#Jawaban No. 2            
def bukaModeDictCsv():
    with open('teori.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

def tulisCsv():
    with open('teori1.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1174007', 'nama': 'tono', 'kelas': 'D4TI2C', 'tanggal lahir': '06/05/1999'})
        writer.writerow({'npm': '1174005', 'nama': 'turbo', 'kelas': 'D4TI2B', 'tanggal lahir': '06/06/1999'})

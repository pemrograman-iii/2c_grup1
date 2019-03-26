# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:14:32 2019

Chapter 4.2

@author: Bakti Qilan
"""
import csv

#No. 1
def membukaCSVmodeList():
    with open('no.1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2], row[3], row[4])  

#No.2
def membukaCSVmodeDict():
    with open('no.1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'], row ['golongan darah'], row['tanggal lahir'])
            
#membuat
def membuatCSV():
    with open('membuatCSV.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow({'npm': '1174083', 'nama': 'Beast', 'kelas': 'D4 TI 2C'})
        writer.writerow({'npm': '1174083', 'nama': 'Goblin', 'kelas': 'D4 TI 2C'})
        
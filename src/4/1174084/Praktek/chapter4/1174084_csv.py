# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:46:00 2019

@author: Reza
"""
import csv

#No. 1
def membukaListCSV():
    with open('data1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2], row[3])


#No. 2            
def membukaDictCSV():
    with open('data1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['nama'], row['npm'], row['kelas'], row['tanggal lahir'])


#Membuat
def membuatCSV():
    with open('data1.csv', mode='w') as csv_file:
        fieldnames = ['nama', 'npm', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'nama': 'Muhammad Reza Syachrani', 'npm': '1174084', 'kelas': 'D4TI2C', 'tanggal lahir': '27/09/1998'})
        writer.writerow({'nama': 'Alvan Apelibel', 'npm': '1174084', 'kelas': 'D4TI2C', 'tanggal lahir': '23-JUN-1994'})
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:25:43 2019

Chapteer 5 Praktek M Arifqi R

@author: Aspire E15
"""
import serial

def ReadSerial():
    ser = serial.Serial("COM3",9600)
    read = ser.readline().decode("utf-8").strip('\n').strip('\r')
    print(read)

ReadSerial()

import csv
def write():
    with open("1174074.csv", mode='w') as nama_file:
        tulis_file = csv.writer(nama_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ser = serial.Serial("COM3",9600)
        read = ser.readline().decode("utf-8").strip('\n').strip('\r')
        tulis_file.writerow([read])
        
write()


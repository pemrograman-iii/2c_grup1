# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:25:00 2019

Chapteer 5 Praktek M Arifqi R

@author: Aspire E15
"""
import serial

def ReadSerialLoop():
    ser = serial.Serial("COM3",9600)
    while (1):
        read = ser.readline().decode("utf-8").strip('\n').strip('\r')
        print(read)
    
ReadSerialLoop()

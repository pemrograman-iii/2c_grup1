# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:05:51 2019

Chapter 5 Praktek

@author: Bakti Qilan
"""

import serial

def ReadSerialLoop():
    ser = serial.Serial("COM3",9600)
    while (1):
        read = ser.readline().decode("utf-8").strip('\n').strip('\r')
        print(read)
    
ReadSerialLoop()
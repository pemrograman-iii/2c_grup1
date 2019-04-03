# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:57:50 2019

@author: ASUS
"""

import serial

def ulang():
    ser = serial.Serial('COM6',9600)
    while(1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
        
ulang()
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:26:37 2019

@author: Reza
"""

import serial

def ReadSerialLoop():
    ser = serial.Serial("COM7",9600)
    while (1):
        read = ser.readline().decode("utf-8").strip('\n').strip('\r')
        print(read)
    
ReadSerialLoop()
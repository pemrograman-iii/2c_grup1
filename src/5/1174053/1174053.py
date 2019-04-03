# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:22:21 2019

@author: ASUS
"""

import serial

def tryExceptError():
    try:
        ser = serial.Serial('COM5',9600)
        print(ser.readline().decode("utf-8)).strip('\n').strip('\r'))
    except TypeError:
        print("Terjadi ketidaksamaan type")
        
tryExceptError()
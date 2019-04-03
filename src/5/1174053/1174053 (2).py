# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:00:55 2019

@author: ASUS
"""

import serial

def tryExcepError():
    try:
        ser = serial.serial('COM5',9600)
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
    except TypeError:
        print ("Terjadi ketidaksamaan type")
        
        
tryExcepError()
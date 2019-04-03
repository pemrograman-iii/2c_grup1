# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:09:28 2019

@author: User
"""

import serial

def tryExceptError():
    try:
        ser = serial.Serial('COM6',9600)
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
    except TypeError:
        print("Terjadi ketidaksamaan type")

tryExceptError()
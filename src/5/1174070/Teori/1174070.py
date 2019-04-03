# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:20:25 2019

@author: User
"""

import serial

def baca():
    ser = serial.Serial("COM6",115200)
    baca = ser.readline()
    print(baca)

baca()
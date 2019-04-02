# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:15:51 2019

Chapter 5

@author: Bakti Qilan
"""

import serial

def CobaArduino():
    seri = serial.Serial("COM5", 115200)
    print(seri.name)  

CobaArduino()
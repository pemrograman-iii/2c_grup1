# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:33:46 2019

@author: Reza
"""

import serial

def PenangananError():
    try:
        ser = serial.Serial('COM7',9600)
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("kesalahan dalam penulisan Syntax")
    except NameError:
        print("Kesalahan dalam penulisan variabel")
    except TypeError:
        print("Kesalahan pada type data")
    except:
        print("Terjadi kesalahan")

PenangananError()
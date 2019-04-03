# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:24:02 2019

Chapteer 5 Praktek M Arifqi R

@author: Aspire E15
"""
import serial

def PenangananError():
    try:
        ser = serial.Serial('COM3',9600)
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("Terjadi Kesalahan Dalam Penulisan Syntax")
    except NameError:
        print("Terjadi Kesalahan Pada Nama Varialble")
    except TypeError:
        print("Terjadi Kesalahan Pada Type Data")
    except:
        print("Terjadi Error")

PenangananError()


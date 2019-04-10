# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:42:26 2019

@author: User
"""

def tryExceptError():
    try:
        from p1174070_bar import batang as bar
    except SyntaxError:
        print("Terjadi kesalahan penulisan")

tryExceptError()
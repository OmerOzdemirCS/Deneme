# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 09:04:50 2022

@author: Burcu Özdemir
"""

from time import sleep
def progress(percent=0, width=30):
    left = width * percent //100
    right = width - left 
    print('\r[', '#' * left, '' * right, ']', f' {percent: .0f}%', sep= '', end= '', flush = True)
     
for i in range(101):
     progress(i)
     sleep(0.1)
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:35:05 2022

@author: Burcu Özdemir
"""

f = open("müşteriler.txt")
# r Read, a append, w write, x create

# print(f.read())
print("************")

# print(f.readline())
# print(f.readline())

for l in f:
    print(l)
    
f.close()


# filetoAppend = open("Talebeler.txt","w")
# filetoAppend.write("\n")
# filetoAppend.write("ömer")
# filetoAppend.write("\n")
# filetoAppend.write("Burcu")
# filetoAppend.close()

import os

if os.path.exists("talebeler.txt"):
    os.remove("Talebeler.txt")
else:
    print("Dosya Yok")
    
os.rmdir("empty")

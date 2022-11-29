# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:59:01 2022

@author: Burcu Özdemir
"""

sehirler = ["Ankara","İstanbul","İzmir","Çorum"]

iteratorum = iter (sehirler)

print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))
print("******************")

for sehir in sehirler:
    print(sehir)
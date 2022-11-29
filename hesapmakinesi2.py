# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 19:55:24 2022

@author: Burcu Özdemir
"""

def topla(sayi1,sayi2):
    return sayi1+sayi2

def cıkar(sayi1,sayi2):
    return sayi1-sayi2

def carp(sayi1,sayi2):
    return sayi1*sayi2

def bol(sayi1,sayi2):
    return sayi1/sayi2


print("Operasyon:")
print("1:Topla")
print("2:Çıkar")
print("3:Çarp")
print("4:Böl")


secenek = input("Operasyon Seçiniz: ")


sayi1 = int(input("1. Sayı gir:"))
sayi2 = int(input("2. Sayı gir:"))


if secenek == "1":
    print("Toplam: "+str(topla(sayi1, sayi2)) )
    
elif secenek == "2":
    print("cıkar: "+str(cıkar(sayi1, sayi2)) )
    
elif secenek == "3":
    print("carp: "+str(carp(sayi1, sayi2)) )
    
elif secenek == "4":
    print("Bölüm: "+str(bol(sayi1, sayi2)) )
    
else:
    print("Gecersiz Seçenek...")
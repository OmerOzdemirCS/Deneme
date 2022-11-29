# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 12:47:26 2022

@author: Burcu Özdemir
"""

try:
    sayi = int (input("Bir sayı giriniz: "))
except ValueError:
    print("Tip uyuşmazlığı: Lütfen bir sayı giriniz.")
    
except ZeroDivisionError:
    print("Payda sıfır olamaz..")
    
except:
    print("Bir hata oluştu..")

print("Bitti")

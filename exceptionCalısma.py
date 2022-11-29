# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:36:08 2022

@author: Burcu Özdemir
"""
import sys
liste = [7,"Ömer",0,3,"6"]

for x in liste:
    try:
        print("Sayı: " + str(x))
        sonuc = 1 / int(x)
        print("Sonuç: " + str(sonuc))
    except ValueError:
        print( str(x) + " Bir sayi değil")
    except ZeroDivisionError:
        print( str(x) + " için sıfıra bölme hatası")
    except:
        print(str(x) + " Hesaplanamadı")
        print("Sistem diyor ki: " + str(sys.exc_info()[0]))
    finally:
        print("İşlemler Bitti")
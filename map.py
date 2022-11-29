# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:17:17 2022

@author: Burcu Özdemir
"""

sayilar = [1,2,3,4,5]

sayilarinKaresi = list(map(lambda sayi: sayi*sayi, sayilar))

# for sayi in sayilar:
#     sayilarKaresi.append(sayi*sayi)
    
sayilarFiltreli = list(filter(lambda sayi: sayi>2, sayilar))
    
print(sayilarinKaresi)
print(sayilarFiltreli)

from functools import reduce
sayilarFaktoriyel = reduce(lambda x,y: x*y, sayilar)

print(sayilarFaktoriyel)
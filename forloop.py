# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 08:35:53 2022

@author: Burcu Özdemir
"""

my_list = [1,2,3,4,5]
for i in my_list:
    if i==6:
        break
    print(f"{i=}")
else:
    print("item not found!")
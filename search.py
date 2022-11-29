# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 01:09:24 2022

@author: Burcu Özdemir
"""
!pip install google -q
from googlesearch import search
# query = "Free Data Science courses"
# for result in search(query, num=10, stop=10, pause=5):
#     print(result)
    
query = "Top 10 Tech YouTube channels"
for result in search(query, num=10, stop=10, pause=5):
    print(result)
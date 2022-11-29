# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:16:57 2022

@author: Burcu Özdemir
"""

import json

with open('users.json') as users:
     data = json.loads(users)
     
     for x in range(6):
          print(data[x]["username"])
          print(data[x]["email"])
          print(data[x]["address"]["street"])
          print(data[x]["address"]["geo"]["lat"])
     
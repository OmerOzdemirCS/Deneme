# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:13:20 2022

@author: Burcu Özdemir
"""

import json

with open("users.json") as users:
    data = json.load(users)
    print(data)
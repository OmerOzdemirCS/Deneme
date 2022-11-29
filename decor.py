# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:05:12 2022

@author: Burcu Özdemir
"""

import functools
def decorator (func_to_decorate):
    @functools.wrap(func_to_decorate)
    def wrapper (*args,**kwargs):
        result=func_to_decorate(*args,**kwargs)
        return result
    return wrapper
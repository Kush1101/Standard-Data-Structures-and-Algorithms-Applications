# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:11:13 2020

@author: DeLL
"""

import random

def random_list(length,a,b):
    return list(random.sample(range(a,b),length))

def random_integer(a,b):
    return random.randint(a,b)

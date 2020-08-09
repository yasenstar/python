#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:25:13 2020

@author: yasen
"""

import numpy as np

# create an array with 10^7 elements
arr = np.arange(1e7)

# converting ndarray to list
larr = arr.tolist()

# Lists cannot by default broadcast,
# so a function is coded to emulate
# what an ndarray can do.

def list_times(alist, scalar):
    for i, val in enumerate(alist):
        alist[i] = val * scalar
    return alist

# Using magic timeit command
timeit arr * 1.1

timeit list_times(larr, 1.1)
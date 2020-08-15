#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 13:22:50 2020

@author: yasen
"""

def size(a,b):
    size = a * b
    return size

p = int(input('Please input Perimeter: '))

for i in range(1, p // 2):
    l = i
    w = (p - 2 * l) // 2
    print('Length x Width = Size: ', l, ' x ', w, ' = ', size(l,w))
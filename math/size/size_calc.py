#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:08:18 2020

@author: yasen
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def size(a,b):
    size = a * b
    return size

print('please input length and width')

length = int(input('length= '))
width = int(input('width= '))

print('=' * 50)

print('Size: ', length, ' x ', width, ' = ', size(length,width))
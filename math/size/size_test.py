#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:42:22 2020

@author: yasen
"""
length = int(input('Hi... please input length: '))
width = int(input('Hi... please input width: '))
print('length is: ', length)
print('width is: ', width)

print('Continue?(Y/N)')

if (input()=='Y'):
    size = length * width
    print('Size= ', size)
else:
    pass
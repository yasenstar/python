# -*- coding: utf-8 -*-
"""
Spyder Editor

Rule 1-2

This is to verify a number with 10 and 99 to see whether below rule is met:
    number = xy
    xy - x - y = ab
    a + b = 9
"""

for xy in range(10,100):
    y = xy % 10
    x = (xy - (xy % 10)) / 10
    ab = xy - x - y
    b = ab % 10
    a = (ab -(ab % 10)) / 10
    if a + b == 9:
        print('Great Job!')
    else:
        print('My God')
next
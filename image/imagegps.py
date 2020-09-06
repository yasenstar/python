# -*- coding: utf-8 -*-
"""
Spyder Editor

Purpose: read image and analyze the property
Date: 2020-09-06
Python Learning QQ Group: 595948765
"""

import re
import exifread

def FindImageGPS(filepath):
    
    gps = {}
    date = ""
    f = open(filepath, 'rb')
    tags = exifread.process_file(f)
    ## Print directly
    # print(tags)
    
    ## Using For Loop but can only print out Key
    # for i in tags:
    #     print(i)
    
    ## Using .items() to convert dict to tuple/list then print key & value
    for key,value in tags.items():
        print(key, value)

if __name__ == '__main__':
    FindImageGPS(r'/home/yasen/Pictures/2018-12-12 031650.jpg')
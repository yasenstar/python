# -*- coding: utf-8 -*-
"""
Spyder Editor

This is to verify a number with 100 and 999 to see whether below rule is met:
    number = xy
    xyz - x - y - z = (xy + 2) * 9
"""

# for i in range(100,1000):
#     if i - i // 100 -i // 10 - i % 10 == ((i - i//10) / 10 + 2 ) * 9:
#         print('Great Job!')
#     else:
#         print('My God')
# next

for xyz in range(400,500):
    z = xyz % 10
    y = (xyz // 10) % 10
    x = xyz // 100
    abc = xyz - x - y - z
    c = abc % 10
    b = (abc // 10) % 10
    a = abc // 100
    # print(xyz, x, y, z, abc, a, b, c, a+b+c)
    if a+b+c == 18:
        print(xyz, x, y, z, abc, a, b, c, a+b+c)
        print('Great Job')

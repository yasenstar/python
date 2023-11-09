# Question: the result of SQRT(a*a+17) is one integer, what is a?
# This is High Middle School entry exam in ShenZhen City
# Date: 2023/11/09

from math import *
for a in range(1,100):
    result = sqrt(a**2 + 37)
    # print(result)
    if (result==round(result)):
        print(a)

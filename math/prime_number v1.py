# Purpose: check whether is Prime number or not in a range of numbers
# Author: Yasen
# Date: May 2021

for i in range(1, 99):
    flag = 0
    for j in range(2, i):
        if (i % j == 0):
            # print(i, "is not a prime number")
            flag = 1
            break
    if (flag == 0):
        print(i, "is a prime number")
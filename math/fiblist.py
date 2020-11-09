#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Date: 2020-11-09
# <<Mastering Algorithms with Python>> 10.3

def fib_list(n):
    if n == 1 or n ==2:
        return 1
    else:
        m = fib_list(n-2) + fib_list(n-1)
        return m

print("*******Please input n for Fib_List*******")
try:
    n = int(input("enter:"))
except ValueError:
    print("Please input one integer and > 0")
    exit()

list = [0]
print(list)
temp = 1
while (temp <= n):
    list.append(fib_list(temp))
    print(list)
    temp += 1

# print(list)
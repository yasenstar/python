# Purpose: check whether is Prime number or not in a range of numbers
# Author: Yasen

print("please input the max range:")
max = int(input())

prime = []

for i in range(1, max):
    flag = 0
    for j in range(2, i):
        if (i % j == 0):
            # print(i, " % ", j, " = 0")
            # print(i, "is not a prime number")
            flag = 1
            break
        # print(i, " % ", j, " <> 0")
    if (flag == 0):
        # print(i, "is a prime number")
        prime.append(i)

print("The prime numbers between 1 and ", max, " are as below:")
print(prime)

"""
Release Notes:
v2: 2021/05/31, add input from keyboard for max range, add array function to store the list of prime
v1: 2021/05/26, draft the basic function
"""
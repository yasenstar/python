# Purpose: use to calculate final principal after x years with compound interest
# Author: Xiaoqi Zhao
# Version: 1.0  Date: 2023/12/17
# Variables:
#   principal: 本金
#   rate: interest rate 年存款利率
#   n: 存款年数
#   result: 结果

principal = 100
rate = 0.015
n = 10
result = principal

for i in range(1,n+1):
    result=result*(1+rate)
    # print("After ", i, " years, principal is ", result)
    print("after {} year, principal is {}".format(i, result))
    
print("*" * 50)
print("final= ",result)

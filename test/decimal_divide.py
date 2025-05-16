from decimal import Decimal, getcontext
getcontext().prec = 4
x = Decimal(1) / Decimal(7)
print(x)
print(int(x * 1000))
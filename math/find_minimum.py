x = 0.0
result = round(x * (x+1) * (x+2) * (x+3), 30)
i = 0.0
while i > -3.0:
    result1 = round(i * (i+1) * (i+2) * (i+3), 30)
    if result1 < result:
        result = result1
        print(i, round(i+1,4), round(i+2,4), round(i+3,4), "\t\t", result)
    i = round(i-0.001, 3)
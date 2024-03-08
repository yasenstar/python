c0 = int(input("please input non-negative and non-zero integer number: "))

steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = int( c0 / 2 )
        print(c0)
    else:
        c0 = int( 3 * c0 + 1 )
        print(c0)
    steps = steps + 1

print(c0)
print("steps = ", steps)
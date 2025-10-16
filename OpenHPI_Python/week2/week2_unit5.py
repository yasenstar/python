r = int(input("Please enter the number of rows int he matrix: "))
c = int(input("Please enter the number of columns in the matrix: "))

print("Enter the matrix values:")

v = [[0 for x in range(c)] for y in range(r)] 

for i in range(r):
    # print(i)
    for j in range(c):
        # print(j)
        v[i][j] = int(input("Value: "))
        print("Value: ", v[i][j])

for i in range(r):
    sum_r = 0
    for j in range(c):
        sum_r += v[i][j]
    print("Sum of row: ", sum_r)
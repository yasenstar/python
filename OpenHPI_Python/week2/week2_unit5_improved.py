r = int(input("Please enter the number of rows int he matrix:"))
c = int(input("Please enter the number of columns in the matrix:"))

print("Enter the matrix values:")

for i in range(r):
    row = []
    for j in range(c):
        val = int(input("Value:"))
        row.append(val)
    print("Sum of row:", sum(row))
with open("numbers.txt") as file:
    lines = file.readlines()

numbers = []
for line in lines:
    numbers.append(int(line))

print("Total = ", sum(numbers))
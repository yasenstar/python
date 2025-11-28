numbers = []
with open("numbers.txt", "r") as file:
    for line in file:
        line = line.strip()
        numbers.append(int(line))

numbers = sorted(numbers)

for i in [-1,-2,-3]:
    print(numbers[i])
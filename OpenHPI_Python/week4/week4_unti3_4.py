with open("numbers.txt") as file:
    lines = file.readlines()

numbers = [int(line) for line in lines]

print("Total = ", sum(numbers))
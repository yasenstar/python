lines = []

with open("numbers.txt", "r") as file:
    for line in file:
        line = line.strip()
        if int(line) % 2 == 0:
            lines.append(line)

with open("even_numbers.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
        
print("List of even numbers created!")
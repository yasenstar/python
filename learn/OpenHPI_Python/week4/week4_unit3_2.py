with open("lorem_ipsum.txt", "r") as file:
    for line in file:
        line = line.strip()
        print(line)
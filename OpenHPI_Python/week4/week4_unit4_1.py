with open("numbers1.txt", "w") as file:
    for i in range(100):
        line = str(i) + "\n"
        file.write(line)
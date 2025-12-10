with open("character.txt", "w") as file:
    for i in range(97, 97+26):
        line = chr(i) + "\n"
        file.write(line)
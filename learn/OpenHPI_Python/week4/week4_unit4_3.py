lines = []
with open("character.txt", "r") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

with open("character_copied.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
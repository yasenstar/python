sentence = input("What sentence should be output?")
letter_to_be_removed = input("Which letter should be removed?")

result = ""
for letter in sentence:
    if letter != letter_to_be_removed:
        result += letter
    if len(result) > 20:
        break
print(result)
import practices.emoji as emoji
def text_to_emoji(text):
    return emoji.emojize(text)

input_text = input("enter emoji aliases: ")

converted_text = text_to_emoji(input_text)

print("result is: ", converted_text)
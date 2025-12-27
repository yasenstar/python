emoji_dict = {
    "happy": "😃",
    "heart": "😍",
    "rotfl": "🤣",
    "smile": "😊",
    "crying": "😭",
    "kiss": "😘",
    "clap": "👏",
    "grin": "😁",
    "fire": "🔥",
    "broken": "💔",
    "think": "🤔",
    "excited": "🤩",
    "boring": "🙄",
    "winking": "😉",
    "ok": "👌",
    "hug": "🤗",
    "cool": "😎",
    "angry": "😠",
    "python": "🐍",
}
sentence = input("Please enter a sentence:")
words = sentence.split()
new_words = []
for word in words:
    if word in emoji_dict:
        word = emoji_dict[word]
    new_words.append(word)
new_sentence = str(new_words[0])
for i in range(1, len(new_words)):
    new_sentence += (" " + new_words[i])
print(new_sentence)
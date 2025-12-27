caesar_dict = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e"
}

t = input("Please enter a sentence: ")
words = t.split()

new_words=[]

for word in words:
    word = word.lower()
    s = ""
    for i in range(len(word)):
        if word[i] in caesar_dict:
            s += (caesar_dict[word[i]])
        else:
            s += word[i]
    new_words.append(s)

sentence = new_words[0]
for i in range(1,len(new_words)):
    sentence += (" "+new_words[i])

print("The encrypted sentence is:", sentence)
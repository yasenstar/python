abc = "abcdefghijklmnopqrstuvwxyz"

Shift_Number = int(input("Please enter the number of places to shift: "))

if 0 <= Shift_Number <= 25:
    Original_Sentence = input("Please enter a sentence: ")

    Words = Original_Sentence.split()

    # print(Words)

    Lower_Words = []

    for word in Words:
        word = word.lower()
        Lower_Words.append(word)

    # print(Lower_Words)

    new_words=[]

    for word in Lower_Words:
        s = ""
        for i in range(len(word)):
            char_index = abc.find(word[i])
            if char_index == -1:
                s += word[i]
            else:
                s += abc[(char_index+Shift_Number) % 25]
        new_words.append(s)

    Encrypted_Sentence = new_words[0]
    for i in range(1,len(new_words)):
        Encrypted_Sentence += (" "+new_words[i])

    print("The encrypted sentence is:", Encrypted_Sentence)

else:
    print("You eed to enter a number between 0 and 25!")
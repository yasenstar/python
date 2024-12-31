# Date: 2024/12/31

import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')   #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 0 for male, 1 for female

engine.say(
    "Happy New Year 2025! "
    "Wishing you a fantastic year ahead! "
)

print("Happy New Year 2025! \
Wishing you a fantastic year ahead!")

engine.runAndWait()

# Documentation: https://pyttsx3.readthedocs.io/en/latest/
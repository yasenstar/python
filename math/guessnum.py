import random

secret = random.randint(1, 100)

print("*" * 60)
print("Let's play, guess a number between 1 to 100.")
print("*" * 60)

tries = 0
guess = 0

while guess != secret and tries <6:
    guess = input("What's your guess? ")
    if guess < secret:
        print("Too small")
    elif guess > secret:
        print("Too big")
    tries = tries + 1

if guess == secret:
    print("wow, you complete the impossible mission!")
else:
    print("You have no more chance...")
    print("Acutally, the secrect is " + str(secret))
# Write a programme where the computer randomly generates a number between 0 and 5.
# The user needs to guess what the number is.
# If the user guesses wrong, tell them their guess is either too high, or too low.

import random

guess = int(input("Guess a number between 0 and 5! "))
randomNumb = random.randrange(1)
if guess == randomNumb:
    print("You guessed " + str(guess))
    print("Your guess is correct.")
else:
    print("You guessed " + str(guess))
    if guess < randomNumb:
        print("Your guess was low.")
    else:
        print("Your guess was high.")
        
print("Correct answer was: " + str(randomNumb))

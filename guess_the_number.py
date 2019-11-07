# Write a programme where the computer randomly generates a number between 0 and 5.
# The user needs to guess what the number is.
# If the user guesses wrong, tell them their guess is either too high, or too low.
import random


guess = int(input("Guess a number between 0 and 5! "))
randomNumb = random.randrange(1)
while guess != randomNumb:
    
    if guess == randomNumb:
        print("You guessed " + str(guess))
        print("Your guess is correct.")
        break
    elif guess < randomNumb:
        print("You guessed low!")
        guess = int(input("Guess a number between 0 and 5! "))
        continue
    elif guess > randomNumb:
        print("Your guessed high!")
        guess = int(input("Guess a number between 0 and 5! "))

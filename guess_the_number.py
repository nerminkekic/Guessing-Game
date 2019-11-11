# Write a programme where the computer randomly generates a number between 0 and 20.
# The user needs to guess what the number is.
# If the user guesses wrong, tell them their guess is either too high, or too low.
import random


# Take input from user
guess = int(input("Guess a number between 0 and 20! "))
# Number of guesses tracking
guess_count = 1
# Generate random number
randomNumb = random.randrange(20)
# Allow user to guess again if first guess is not correct
# Also check for conditions and let user know if they guessed high or low
while guess != randomNumb:
    guess_count += 1
    if guess < randomNumb:
        print("You guessed low!")
        guess = int(input("Try another guess. "))
    elif guess > randomNumb:
        print("Your guessed high!")
        guess = int(input("Try another guess. "))
print("You have guessed correct. YOU WIN!")
print(f"Total number of guesses: {guess_count}")

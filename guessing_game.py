# Guessing game - Asks user to provide a "level." CPU will pick a random number between 1 and the value of the level specified by the user. User then attempts to guess the number.

import random
import sys

user_level = input("Level: ")                                       # the number entered by the user as the upper bound of the number to be guessed

while True:
    if user_level.isnumeric() == True and int(user_level) > 0:
        int_user_level = int(user_level)                            # converts user input to int and assigns to int_user_level
        cpu_guess = random.randint(1, int_user_level)               # random number between 1 and user_level the CPU picks for purposes of guessing
        break
    else:
        user_level = input("Level: ")                               # if user_level is invalid, re-prompt for input and assign to user_level
        continue

user_guess = input("Guess: ")

while True:
    try:
        if user_guess.isnumeric() == True and int(user_guess) > 0:
            if user_guess == cpu_guess:
                print("Just right!")
                sys.exit()                                          # exits once the user guesses the correct number
            elif user_guess > cpu_guess:
                print("Too large!")
                user_guess = int(input("Guess: "))
                continue
            elif user_guess < cpu_guess:
                print("Too small!")
                user_guess = int(input("Guess: "))
                continue
        else:
            user_guess = input("Level: ")                           # if user_guess is invalid, re-prompt for input and assign to user_guess
            continue
    except ValueError:
        user_guess = input("Level: ")                               # if user_guess is invalid, re-prompt for input and assign to user_guess
            continue

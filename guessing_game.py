# Guessing game - Asks user to provide a "level." CPU will pick a random number between 1 and the value of the level specified by the user. User then attempts to guess the number.

import random
import sys

user_level = input("Level: ")                                       # prompts user to enter a number to be the upper bound of the random number to be guessed

while True:
    if user_level.isnumeric() == True and int(user_level) > 0:
        int_user_level = int(user_level)                            # converts user input to int and assigns to int_user_level
        cpu_guess = random.randint(1, int_user_level)               # random number between 1 and user_level the CPU picks for purposes of guessing
        break
    else:
        user_level = input("Level: ")                               # if user_level is invalid, re-prompt for input and assign to user_level
        continue

while True:
user_guess = input("Guess: ")                                       # prompts user for their first guess
    if user_guess.isnumeric() == True and int(user_guess) > 0:  # validates guess if a positive number
        if int(user_guess) == cpu_guess:
            print("Just right!")
            sys.exit()                                          # exits once the user guesses the correct number
        elif int(user_guess) > cpu_guess:
            print("Too large!")
            continue
        elif int(user_guess) < cpu_guess:
            print("Too small!")
            continue
        else:
            continue

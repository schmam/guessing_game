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

while True:
    user_guess = input("Guess: ")
    if int(user_guess) == cpu_guess:
        print("Just right!")
        break
    elif int(user_guess) > cpu_guess:
        print("Too large!")
        continue
    elif int(user_guess) < cpu_guess:
        print("Too small!")
        continue

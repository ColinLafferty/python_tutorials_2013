#!/usr/bin/env python
import random
'''\
The computer will pick a number between 1 and 100. (You can choose any high 
number you want.) The purpose of the game is to guess the number the computer 
picked in as few guesses as possible.

source:http://openbookproject.net/pybiblio/practice/\
'''
high_or_low = {True: "Too high. Try again:",
               False: "Too low. Try again: "}


def main():
    choice = random.randrange(1, 100)
    user_choice = -1
    while user_choice != choice:
        user_choice = int(input("Please enter your choice: "))
        is_high = user_choice > choice
        if user_choice == choice:
            break
        print(high_or_low[is_high])
    print("You guessed {0} correctly".format(choice))

if __name__ == "__main__":
    main()

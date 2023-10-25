#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Oct 25, 2023
# This program will ask the user
# for a number and will tell them
# if they guessed correctly using random number

import random


def main():
    # Get the user guess
    print("This program will ask the user for a number between 1 and 9 and ")
    print("then it will display if they guessed correctly or not.")

    user_guess_as_string = input("Please enter your guess between 1 and 9: ")

    # create generator for correct_guess
    correct_guess = random.randint(1, 10)

    # initialize variable
    user_guess_as_integer = None

    # Try catch statement
    try:
        user_guess_as_integer = int(user_guess_as_string)

        # Check if the user guess is equal to correct guess
        if user_guess_as_integer == correct_guess:
            # Display if the user is right
            print("\nCongratulations, you guessed correctly!")

        else:
            # Display if the user is wrong
            print(
                "\nPlease guess again, the correct number was {}".format(correct_guess)
            )

    # Checking it the if the input is a string and if it is then telling user
    except Exception:
        print("\n{} is not a integer".format(user_guess_as_string))

    # Always display this to user
    finally:
        print("\nThanks for playing!")


if __name__ == "__main__":
    main()

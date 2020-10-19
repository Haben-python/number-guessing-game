"""
---------------------------------
Python Web Development Techdegree
Project 1 - Number Guessing Game
---------------------------------
"""

import random


def start_game():
    #Displays welcome message to user
    print("-" * 38)
    print(" Welcome to the Number Guessing Game")
    print("-" * 38)
    #Stores highscores, attempts, and generates a random number
    answer = random.randint(1, 10)
    attempts = 0
    highscore = []
    #Prompts user for a guess and evaluates if that guess is either lower, higher, or equivalent to the correct answer
    while True:
        guess = input("Please guess a number between 1 and 10: ")
        guess = int(guess)
        attempts += 1
        if guess > answer:
            print("It's lower")
        elif guess < answer:
            print("It's higher")
        elif guess == answer:
            #Prompts user if they want to play again, displays the best score of all-time
            #Ends program if user decides to not play anymore
            print("\n")
            print("You got it! It took you {} tries.".format(attempts))
            highscore.append(attempts)
            play_again = input("Would you like to play again? Y/N: ")
            attempts = 0
            answer = random.randint(1, 10)
            if play_again.upper() == "Y":
                print("The HIHGSCORE is {} attempts to find the correct answer.".format(min(highscore)))
                continue
            elif play_again.upper() == "N":
                break
    print("Closing game, Thank you for playing!")


#Starts the program
start_game()

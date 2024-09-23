# Name of Program: Dice Rolling Guessing Game
# Description of Program: This program is a tiny game that generates dice rolls, and allows the user to guess what was rolled.

# Date Written: 2023-11-01
# Author: William Young

##########################::::::::::    CONSTANTS    :::::::::::####################################

DICE_GUESS_FORMAT = r'^\d{1}$'

while True: # REPEAT PROGRAM LOOP

    import random #Library used for randomizing values
    import re     #Handy library used for comparing string formats

    DiceRoll = int(random.randint(0,6)) #Randomize a number between 1, and 6. The first value as an integer will never be allowed.

    #print(DiceRoll) #Uncomment Only for Debugging!

##########################::::::::::   USER INPUTS   :::::::::::####################################

    while True: #Asking the user to guess a number between 1 and 6. Asking them to retry if they do not enter a single digit.
 
        PlayersGuess = input("A single Dice has been rolled. Guess a number between 1 and 6: ")
        if re.match(DICE_GUESS_FORMAT, PlayersGuess):
            break
        else:
            print("You must guess a number between 1 and 6. Please try again.")

##########################::::::::::      OUTPUT     :::::::::::####################################

    PlayersGuess = int(PlayersGuess)

    if PlayersGuess == DiceRoll:
        print("Congratulations! You guessed correctly!")
    else:
        print("Oops! You guessed incorrectly!")

##########################::::::::::  REPEAT PROMPT  :::::::::::####################################

    Continue = input("Do you want to play again? (Y/N): ").upper()
    if Continue == "N":
        break

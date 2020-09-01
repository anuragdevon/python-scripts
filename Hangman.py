# Python code for hangman
# Anurag Kar-2020
import sys
import random

print("\n\n----------------------------------------")
print("         WELCOME TO HANGMAN")
print("----------------------------------------")
print("       Press enter to continue")
input()

print("Instructions :")
print(">> From the choice of words given, computer will choose random any word.\n   Your Job is guess the selected word.\n   After every guessing, some characters will be displayed!...\n   Once all chacters gets displayed, You Lose!\n\n             BEST OF LUCK!!")
print("       Press enter to continue")
input()

name = input("\nPlease enter the player name : ")

words = ["pewdiepie", "python", "universe", "github", "helloworld"]  # Currently stored words

word = random.choice(words) # Choice random selection
print("OK " + name + ", get ready...\n")
print("\n--------The game begins!!--------\n")

print("Please guess the charcters :")

# Delclaring guesses, and intilizing turns to 10
guesses = ""
turns = 10

# For executing the gussing logic
while(turns > 0):
    failed = 0
    for char in word:
        if char in guesses:
            print(char)        # will print the guessed correct character
        else:
            print("_")
            failed += 1   # increamenting failed for getting wrong
    if failed == 0:
        print("Congrats!! You won!!\n")
        print("The word is : ", word)
        break

    guess = input("Guess the character: ")
    guesses += guess                         # increamenting the guesses
   
    if guess not in word:                    #presetting the turn for condition
        turns -= 1
    print("Oops!, Wrong\n")
    print("Now You have", +turns, "more guesses...")

    if turns == 0:
        print("No more guesses")
        print("Ahh!, You are hanged :(\n")

print("\n\n----------------------------------------")
print("     Thankyou for trying..see u soon :)")
print("----------------------------------------")
print("         Press enter to exit")
input()
# Exiting
sys.exit(0)
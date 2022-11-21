#     Assignment | Assignment 3-3
#  Program Title | Hangman
#                |
#     Written by | Khurram Shaikh
#           Date | Monday, November 21, 2022
#                |
#    Description | This program simulates the popular game of Hangman.
#                | User is asked to enter a puzzle and category, or 
#                | generate a random word. Based on correct guesses of
#                | the word opposing user wins or loses. Gallows are
#                | drawn as an enhancement after incorrect guesses are 
#                | made.

import random

def hangmanArt():
    """Displays Hangman art based on amount 
    of wrong guesses made by user.
    """
    if (wrong==1):
        print("  +----+")
        print("  O    |")
        print("       |")
        print("       |")
        print("       |")
        print("     =====")
    elif (wrong==2):
        print("  +----+")
        print("  O    |")
        print("  |    |")
        print("       |")
        print("       |")
        print("     =====")
    elif (wrong==3):
        print("  +----+")
        print("  O    |")
        print(" /|    |")
        print("       |")
        print("       |")
        print("     =====")
    elif (wrong==4):
        print("  +----+")
        print("  O    |")
        print(" /|\   |")
        print("       |")
        print("       |")
        print("     =====")
    elif (wrong==5):
        print("  +----+")
        print("  O    |")
        print(" /|\   |")
        print(" /     |")
        print("       |")
        print("     =====")
    else:
        print("  +----+")
        print("  O    |")
        print(" /|\   |")
        print(" / \   |")
        print("       |")
        print("     =====")
wrong=0
prevGuess=""

# Initialize random words as a list
randWords="Canada Basketball Panda Bennies Fallacious Happiness Mandarin Computers Python Blanket Austria Croatia Pizza Trigonometry Snow Christmas Apples Bannana Brazil Algorithm Pseudocode".split()
category=""
print('{:-^80s}'.format('Hangman!'))

# Ask user for puzzle
puzzle=input("Enter puzzle ('r' to select a random word): ").upper()

# If user enters 'R' generate a random word
if (puzzle=='R'):
    
    # Generate a random number from 0 to length
    # random words list - 1
    randWordNum=random.randint(0,len(randWords)-1)
    
    # Set puzzle to random words list referenced to
    # generated random word number 
    puzzle=randWords[randWordNum].upper()
else:
    
    # Ask user for category
    category=input("Enter category: ")
hidden=puzzle

# Start counted loop to create hidden
for x in range(len(hidden)):
    if (hidden[x].isalpha()):
        hidden=hidden[:x]+'_'+hidden[x+1:]

# Start infinite loop
while True:
    print()
    
    # Start counted loop to display hidden spaced out
    for x in range(len(hidden)):
        print(hidden[x],end=" ")
    
    # If category is not a blank string display category
    if (category!=""):
        print("\nSelected category is {}".format(category))
    
    # Start infinite loop in case user enters invalid value
    while True:
        
        # Ask user for guess
        guess=input("\nEnter guess ('1' to solve puzzle): ").upper()

        # If guess is not in the alphabet and a previous guess or '1'
        # display error message
        if (guess.isalpha() and prevGuess.find(guess)==-1 or guess=='1'):
            break
        print("Error, invalid character! Enter a guess between 'A' and 'Z' or '1'.")
        
        # If previous guess was made notify user
        if (prevGuess.find(guess)!=-1):
            print("Already guessed: '{}', make another guess.".format(prevGuess))

    # Start counted loop to replace hidden with correct guess
    for x in range(len(puzzle)):
        
        # If puzzle referenced to counted character 
        # is in guess 
        if (guess.find(puzzle[x])!=-1):
            
            # Replace hidden with correct guess
            hidden=hidden[:x]+puzzle[x]+hidden[x+1:]
            prevGuess+=" "+guess+" "
    
    # If user solves puzzle or enters '1'
    if (hidden==puzzle or guess=='1'):
        
        # Display winning message and wrong guesses
        print("You win! It took {} wrong guess".format(wrong),end="")
        if (wrong>1):
            print("es")
        
        # Display solved puzzle
        print("\nSolved puzzle is: \n{}".format(' '.join(puzzle)))
        break
    
    # Else if user enters an incorrect guess
    elif (hidden.count(guess)==0):
            
            # Add one to wrong
            wrong+=1
            
            # Display message for making a mistake
            print("Sorry that is incorrect, '{}' is not in the puzzle.\nThis is wrong guess #{}".format(guess,wrong))
            
            # Call function to display a Hangman art based on mistakes made
            hangmanArt()
            prevGuess+=" "+guess+" "
            
            # If six wrong guesses are made exit program and display puzzle
            if (wrong==6):
                print("You lose!\nSolved puzzle is:")
                print(' '.join(puzzle))
                break
    
    # Under any other condition display count of remaining characters 
    else:
        print("{} remaining character".format(hidden.count("_")),end="")
        if (hidden.count("_")>1):
            print("s")
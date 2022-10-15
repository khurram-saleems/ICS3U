#     Assignment | Assignment 2-2
#  Program Title | Pick a number
#                |
#     Written by | Khurram Shaikh
#           Date | Wednesday, October 12, 2022
#                |
#    Description | This program asks the user for their name and
#                | a guess for a random number between 1 and 100.
#                | Includes personalized messages based on guess,
#                | continues to loop 10 time or until correct guess
#                | is made.

import random

# Ask user for name
name = input("\nPlease enter your name: ")

# Generate random number from 1 to 100
randNum = random.randint(1,100)

# Starts a for loop
for guessCount in range (1,11):
    
    # Start infinite loop in case user enters invalid value
    while True:
        
        # Ask user for random number
        guess = int(input("\n{} enter a random number between 1 and 100: ".format(name)))
        
        # If random number is between 1 and 100 exit loop
        if (guess >= 1 and guess <=100):
            break
        
        # Display error message 
        print("Error! Invalid value, {} enter a number that is between 1 and 100.".format(name))
    
    # If guess is equal to random number 
    # Display that they have guessed correctly and then
    # Exit loop
    if (guess == randNum):
        print("\nNice job {}! You guessed correctly.".format(name))
        break    
    
    # Else if guess is less than random number
    # Display that the random number is higher
    elif (guess < randNum):
        print("\n{}, the random number is higher.".format(name))
    
    # Else display that the random number is lower
    else:
        print("\n{}, the random number is lower." .format(name))

# Display amount of times user guessed 
print("\n{}, you guessed {} times!".format(name,guessCount))
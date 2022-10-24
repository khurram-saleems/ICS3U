#     Assignment | Assignment 2-4
#  Program Title | Craps!
#                |
#     Written by | Khurram Shaikh
#           Date | Tuesday, October 25, 2022
#                |
#    Description | This program asks user for their name
#                | and bet. Generates and adds two random
#                | numbers. User wins or loses money based 
#                | on rolled dice. Program continues to run
#                | or exit based on user. Simulates dice
#                | game of Craps.

import random    
def diceRoll():
    """Generates two random numbers from 1,6
    and adds them together.
    """

    # Globalize dice1, dice2 and roll
    # to access and modify outside the
    # function  
    global dice1
    global dice2 
    global roll
    dice1,dice2=random.randint(1,6),random.randint(1,6)
    roll=dice1+dice2    
def asciiArt(n):
    """Displays ASCII art of the dice, based on 
    generated number.
    n: randomly generated dice values
    """
    if (n==1):
        print(" ------- ")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print(" ------- ")
    elif (n==2):
        print(" ------- ")
        print("|      o|")
        print("|       |")
        print("|o      |")
        print(" ------- ")
    elif (n==3):
        print(" ------- ")
        print("|      o|")
        print("|   o   |")
        print("|o      |")
        print(" ------- ")
    elif (n==4):
        print(" ------- ")
        print("|o     o|")
        print("|       |")
        print("|o     o|")
        print(" ------- ")
    elif (n==5):
        print(" ------- ")
        print("|o     o|")
        print("|   o   |")
        print("|o     o|")
        print(" ------- ")
    else:
        print(" ------- ")
        print("|o     o|")
        print("|o     o|")
        print("|o     o|")
        print(" ------- ")
# Initialize money to 100 and point to 0
money,point=100,0
print("{:*^80s}".format("Las Vegas Craps Casino"))

# Display ASCII art
print("--------------")
print("|   ________ |")
print("|   |Craps!| |")
print("|   -------- |")
print("|    ----    |")
print("|   | o  |   |")
print("|   |(|\o|   |")
print("|   |/ \ |   |")
print("|    ----    |")
print("--------------")

# Ask user for their name
name=input("Enter your name: ")
print("\nWelcome to Craps {}!\nYou have ${}.".format(name,money))

# Start infinite loop
while True:
    
    # Start infinite loop in case user enters invalid value
    while True:
        
        # Ask for amount to bet 
        # If bet is greater than money or bet is less than 0
        # Display error message
        bet=int(input("\n{}, how much would you like to bet (0 to quit)? ".format(name)))
        if (bet<=money and bet>=0):
            break
        print("Error, invalid value! Enter amount that you can afford and not less than 0.")
    
    # If user enter's 0 as bet, exit program
    if (bet==0):
        break
    
    # Calls function to generate and add random numbers
    # of two dices
    diceRoll()

    # Display the two random number's and the roll
    print("\nYou rolled a {} and a {}, that's {} {}.".format(dice1,dice2,roll,name))
    
    # Calls function while passing in the value 
    # of two dice, displays ASCII art of dice
    asciiArt(dice1)
    asciiArt(dice2)
    
    # If roll is 7 or 11 add the bet to total money 
    # and notify user of winning
    # Display total money
    if (roll==7 or roll==11):
        money+=bet
        print("You win!")
        print("\n{}, you now have ${}.".format(name,money))
    
    # Else if roll is 2, 3, or 12 subtract the bet from total money
    # and notify user of winning
    # Display total money
    elif (roll==2 or roll==3 or roll==12):
        money-=bet
        print("You lose!")
        print("\n{}, you now have ${}.".format(name,money))

    # Under any other condition set point equal to roll
    else:
        point=roll
    
    # Start infinite loop
    while True:
        resume=input("Enter any key to roll again. ")
        
        # Calls function to generate and add dice
        diceRoll()
        print("\nYou rolled a {} and a {}, that's {} {}.".format(dice1,dice2,roll,name))
        
        # Calls function to display ASCII art 
        # for the two dice
        asciiArt(dice1)
        asciiArt(dice2)
    
        # If roll is 7 or 11 subtract bet from total money
        # Notify user of losing and exit loop
        if (roll==7 or roll==11):
            money-=bet
            print("You lose!")
            break
        
        # Else if roll is point add bet to total money
        # Notify user of winning and exit loop
        elif (roll==point):
            money+=bet
            print("That's your point, you won!")
            break
    
    # Display money left
    print("\n{}, you now have ${}.".format(name,money))
    
    # If user has no money notify that they are bankrupt
    if (money==0):
        print("You are bankrupt!")
    
    elif (money>100):
        print("Wow, you have more than you started with!")
    
    # Start infinite loop in case user enters invalid value 
    while True:
        # Ask user if they would like to roll again
        reRoll=input("\nWould you like to roll again ('y' or 'n')? ")[0].lower()
        if (reRoll=='y' or reRoll=='n'):
            break
        print("Error, invalid response. Enter 'y' or 'n'.")
    
    # If user enters 'n' exit program
    if (reRoll=='n'):
        print("\n--------------")
        print("|   ________ |")
        print("|   |Craps!| |")
        print("|   -------- |")
        print("|    ----    |")
        print("|   | o  |   |")
        print("|   |/|)o|   |")
        print("|   |/ \ |   |")
        print("|    ----    |")
        print("--------------")
        break

# Display parting message
print("\nThanks for playing Craps, hope you enjoyed your time {}!".format(name))
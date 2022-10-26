#     Assignment | Assignment 2-4
#  Program Title | Craps Dice Game
#                |
#     Written by | Khurram Shaikh
#           Date | Tuesday, October 25, 2022
#                |
#    Description | This program asks user for their name and bet. Generates 
#                | and adds two random numbers. User wins or loses money 
#                | based on rolled dice. Program continues to run or exit 
#                | based on user. Simulates dice game of Craps.

import random    
def diceRoll():
    """Generates two random numbers from 1,6
    and adds them together.

    Returns: 
        total: addition of random numbers from 1,6
        rand1: random number from 1,6
        rand2: random number from 1,6
    """
    rand1,rand2=random.randint(1,6),random.randint(1,6)
    total=rand1+rand2
    return total,rand1,rand2  
def asciiArt(diceVal):
    """Displays ASCII art of the dice, based on 
    generated number.
    
    diceVal: randomly generated dice values
    """
    if (diceVal==1):
        print(" ------- ")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print(" ------- ")
    elif (diceVal==2):
        print(" ------- ")
        print("|      o|")
        print("|       |")
        print("|o      |")
        print(" ------- ")
    elif (diceVal==3):
        print(" ------- ")
        print("|      o|")
        print("|   o   |")
        print("|o      |")
        print(" ------- ")
    elif (diceVal==4):
        print(" ------- ")
        print("|o     o|")
        print("|       |")
        print("|o     o|")
        print(" ------- ")
    elif (diceVal==5):
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

# Initialize money to 100 and attempt to 0
attempt,money=0,100
print("{:*^80s}".format("Las Vegas Craps Casino"))

# Display opening ASCII art
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

        # Ask for betting amount
        bet=int(input("\n{}, how much would you like to bet (0 to quit)? ".format(name)))

        # If bet is greater than money or bet is less than 0 
        # display error message
        if (bet<=money and bet>=0):
            break
        print("Error, invalid value! Enter amount that you can afford and not less than 0 {}.".format(name))
    
    # If bet is equal to 0 exit program
    if (bet==0):
        break
    
    # Calls function to generate and add dice
    roll,dice1,dice2=diceRoll()

    # Adds one and stores in attempt
    attempt+=1
    
    # Display the two random numbers and the roll
    print("\nYou rolled a {} and a {}, that's {} {}.".format(dice1,dice2,roll,name))
    
    # Calls function to display ASCII dice art
    # Rolled dice values passed in as arguments
    asciiArt(dice1)
    asciiArt(dice2)
    
    # If roll is 7 or 11 add the bet to total money 
    # and display winning message
    if (roll==7 or roll==11):
        money+=bet
        print("You win!")
    
    # Else if roll is 2, 3 or 12 subtract the bet from total money
    # and display losing message
    elif (roll==2 or roll==3 or roll==12):
        money-=bet
        print("You lose!")

    # Under any other condition set point equal to roll
    else:
        point=roll
    
        # Start infinite loop
        while True:
            input("Press [Enter] or any key to roll again: ")
        
            # Calls function to generate and add dice
            roll,dice1,dice2=diceRoll()

            # Adds one and stores in attempt
            attempt+=1
            
            # Display the two random numbers and the roll
            print("\nYou rolled a {} and a {}, that's {} {}.".format(dice1,dice2,roll,name))
            
            # Calls function to display ASCII art for the two dice
            asciiArt(dice1)
            asciiArt(dice2)

            # If roll is 7 or 11 subtract bet from total money 
            # notify user of losing and exit loop
            if (roll==7 or roll==11):
                money-=bet
                print("You lose!")
                break
            
            # Else if roll is point add bet to total money
            # notify user of winning and exit loop
            elif (roll==point):
                money+=bet
                print("That's your point, you won!")
                break
        
    # Display remaining money and total rolls made
    print("\n{}, you now have ${} and a total of {} roll".format(name,money,attempt),end="")
    if (attempt>1):
        print("s!")

    # If user has no money notify that they are bankrupt
    if (money==0):
        print("\nYou are bankrupt!")

    # Else if money is greater than 100 notify that they
    # have more than original amount
    elif (money>100):
        print("\nWow, you have more than you started with!")

    # Start infinite loop in case user enters invalid value 
    while True:

        # Ask user if they would like to roll again
        # and all responses lower cased
        reRoll=input("\n\nWould you like to roll again ('y' or 'n')? ")[0].lower()
        
        # If does not enter 'y' or 'n' display error message
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
        print("|   ||/  |   |")
        print("|    ----    |")
        print("--------------")
        break
        
# Display parting message
print("\nThanks for playing Craps, hope you enjoyed your time {}!\n".format(name))
#     Assignment | Assignment 2-4
#  Program Title | Craps!
#                |
#     Written by | Khurram Shaikh
#           Date | Tuesday, October 25, 2022
#                |
#    Description | This program simulates the game Craps.

import random    

def diceAdd():

def diceRoll():
    # Generate two random numbers from 1,6
    dice1,dice2=random.randint(1,6),random.randint(1,6)
    
    # Add and store in roll
    roll=dice1+dice2
    return roll

def asciiArt():
    if (roll==1):
        print(" ------- ")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print(" ------- ")
    elif (roll==2):
        print(" ------- ")
        print("|      o|")
        print("|       |")
        print("|o      |")
        print(" ------- ")
    elif (roll==3):
        print(" ------- ")
        print("|      o|")
        print("|   o   |")
        print("|o      |")
        print(" ------- ")
    elif (roll==4):
        print(" ------- ")
        print("|o     o|")
        print("|       |")
        print("|o     o|")
        print(" ------- ")
    elif (roll==5):
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
money=100
point=0
# Display title
print("{:-^80s}".format("Las Vegas Craps Casino"))

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
    
    # Call dice roll function 
    total=diceRoll(dice1,dice2,roll)
    print(total)
    
    # Display the two random number's and the roll
    print("\nYou rolled a {} and a {}, that's {} {}.".format(dice1,dice2,roll,name))
    asciiArt()
    
    # If roll is 7 or 11 add the bet to total money 
    # and notify user of winning
    if (roll==7 or roll==11):
        money+=bet
        print("You win!")
    
    # Else if roll is 2, 3, or 12 subtract the bet from total money
    # and notify user of winning
    elif (roll==2 or roll==3 or roll==12):
        money-=bet
        print("You lose!")
    
    # Else if roll wins or loses money
    # Update user with amount left
    elif(roll==7 or roll==11 or roll==2 or roll==3 or roll==12):
        print("\n{}, you now have ${}.".format(name,money))
    
    # Under any other condition
    # set point equal to roll
    else:
        point=roll
    
    # Start infinite loop
    while True:
        resume=input("Enter any key to roll again.")
        diceRoll(dice1,dice2,roll)
        print("\nYou rolled a {} and a {}, that's {} {}.".format(dice1,dice2,roll,name))
        asciiArt()
        
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

    # Ask user if they would like to roll again
    reRoll=input("\nWould you like to roll again ('y' or 'n')? ")[0].lower()
    
    # If user enters 'n' exit program
    if (reRoll=='n'):
        break

# Display parting message
print("\nThanks for playing Craps, hope you enjoyed your time {}!".format(name))
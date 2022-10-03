# 06 Questions
# Input Practice
#
# Khurram Shaikh
# Saturday, September 24, 2022
#
# Program prompts user to input various values user 
# input is then displayed at the end of the program. 

# Asks user how they are feeling and displays how they are feeling
feel = input("Hello, how are you? ")
print("You are feeling",feel)
print()

# Asks user for number to square
number=int(input("Give me a number to square: "))
numberSq=number**2
print("{} squared is {}.".format(number,numberSq))
print()

# Asks user to calculate change if the price is $10.50 and money given is $15.35, $20.25
price = 10.5
change1,change2=float(input("Price of item is $10.50, money given is $15.35. Enter change: ")),float(input("Price of item is $10.50, money given is $20.25. Enter change: "))
print("You entered ${} as the change for the first item and ${} as change for the second item.".format(change1,change2) )
print()

# Asks user to enter their shoe size and displays the result back
shoe_size=float(input("Enter your shoe size: "))
print("Your shoe size it {}.".format(shoe_size))
print()

# Asks user to enter as many characters of Euler's number as possible
eulersNum=float(input("Enter as many characters of Euler's number as possible (starts from 2.7..): "))
print("You entered {}, as Euler's number.".format(eulersNum))
print()

# Asks user if 1+1=2 and stores result as a integer data type
eqn_verify=input("Is 1+1=2? ")
print("You entered {} as an answer for if 1+1=2.".format(eqn_verify))
print()

# Asks user how long they go to work/school in a day
time_working=float(input("In hours only, enter the amount of time you work or go to school in a day: "))
print("You work or go to school for {} hours.\n".format(time_working))

# Displays all responses with one print and .format() statement 
print('You are feeling: {}. {} is the number to be squared. Entered ${} as change for first item. Entered ${} as change for second item. Shoe size is: {}. You entered Euler\'s Number as: {}. Response to if "1+1=2"{}. You work {} hours a day.'.format(feel,number,change1,change2,shoe_size,eulersNum,eqn_verify,time_working))
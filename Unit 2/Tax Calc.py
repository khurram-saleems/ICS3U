# 01 Practice Programs 1 
# Program 1: Tax Calculator
#
# Khurram Shaikh
# Friday, October 7, 2022
#
# This program asks user to enter the cost of 
# food and drinks, then calculates the total.
# If total is greater than 15, tax is displayed
# and included in the total

# Start infinite loop in case user enters invalid value
while True:
    
    # Ask user for cost of food
    foodCost = float(input("Enter the cost of food: "))
    
    # If cost is less than 5.99 display error message
    if (foodCost>=5.99):
        break
    print("Error! Food items are all $5.99 or greater.")

# Start infinite loop incase user enters invalid value
while True:
    
    # Ask user for drink cost
    drinkCost = float(input("Enter the drink cost: "))
    
    # If cost is less than 1.99 display error message
    if (drinkCost>=1.99):
        break
    print("Error! Drink items are $1.99 or greater.")

# Calculate total cost
total=foodCost+drinkCost

# If total is greater than 15 calculate tax,
# and display tax and add it to total
if (total>15):
    tax=0.13*total
    total+=tax
    print("Tax is ${:.2f}.".format(tax))
    print("Final total is ${:.2f}".format(total))

# Under any other condition display total to 
# two decimal places
else:
    print("Total cost is ${:.2f}, please pay up!".format(total))

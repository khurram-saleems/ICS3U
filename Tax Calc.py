# 01 Practice Programs 1 
# Program 1: Tax Calculator
#
# Khurram Shaikh
# Friday, September 30, 2022
#
# This program asks user to enter the cost of 
# food and drinks, then calculates the total.
# If total is greater than 15, tax is displayed
# and included in the total

print("{:-^80}".format(""))
foodCost = float(input("Enter the cost of food: "))
drinkCost = float(input("Enter the drink cost: "))
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
# 01 Practice Programs 1 
# Program 4: Class Divider
#
# Khurram Shaikh
# Monday, October 3, 2022
#
# This program divides the user into two groups
# based on the starting letter of their last name.
# Experiments with concepts from string 
# manipulation.

# Ask user for last name 
lastName=input("Enter your last name: ")

# If the starting character of last name
# is between 'A' and 'H' notify group 1  
if (lastName>="A" and lastName<="H"):
    print("\nYou are in group 1, your last name is between 'A' and 'H'")

# If the starting chaaracter of last name 
# is betewen 'I' and 'Z' notify group 2
elif(lastName>="I" and lastName<="Z"):
    print("\nYou are in group 2, your last name is between 'I' and 'Z'.")
# 10 Practice Programs 2
# Program 5: Last First Name 
#
# Khurram Shaikh
# Friday, October 14, 2022
#
# This program asks the user to enter 10 names, outputs 
# the name that is alphebetically last.

lastName=""

# Start counted loop to repeat 10 times
for x in range(10):
    
    # Ask user for first name
    name=input("Enter your first name: ")
    
    # If name greater than low 
    # Make name equal low
    if (name>lastName):    
        lastName=name
print("The name that is alphebetically last is {}".format(lastName))
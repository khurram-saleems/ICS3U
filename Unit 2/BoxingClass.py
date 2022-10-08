# 06 Practice Programs 1 
# Program 2: Boxing Class
#
# Khurram Shaikh
# Friday, October 7, 2022
#
# This program classifies athletes into three classes
# entirely based on weight.

# Start infinite loop in case user enters invalid value
while True:
    
    # Ask user for weight
    weight=int(input("Enter your weight in kilograms: "))
    
    # If weight is less than 40 kg display error message
    if (weight>=40):
        break
    print("Error! You must be over 40 KG to enter the tournament.")

# If weight is greater than 80 kg notify heavyweight class
if (weight>80):
    print("You are in the heavyweight class. At {} kg.".format(weight))

# Else if weight is between 60 kg and 80 kg
# notify of medium class
elif (weight>=60 and weight<=80):
    print("You are in the medium class. At {} kg.".format(weight))

# Under any other condition notify that they are in lightclass
else:
    print("You are in the lightweight class. At {} kg.".format(weight))

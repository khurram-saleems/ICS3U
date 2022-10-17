# 06 Practice Programs 1 
# Program 2: Boxing Class
#
# Khurram Shaikh
# Friday, October 14, 2022
#
# This program classifies athletes into three classes
# entirely based on weight.

heavy,medium,light=0,0,0

# Start a counted loop for the program to run 24 times
for x in range(25):
    
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
        heavy+=1
    # Else if weight is between 60 kg and 80 kg
    # notify of medium class
    elif (weight>=60 and weight<=80):
        print("You are in the medium class. At {} kg.".format(weight))
        medium+=1
    # Under any other condition notify that they are in lightclass
    else:
        print("You are in the lightweight class. At {} kg.".format(weight))
        light+=1
total=heavy+medium+light
print("For the heavy category {} registered, medium {}, and light {}. Toal people that registered: {}")

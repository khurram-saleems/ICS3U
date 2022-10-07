#     Assignment | Assignment 2-1
#  Program Title | Air Canada Aeroplan Miles Customer Service 
#                |
#     Written by | Khurram Shaikh
#           Date | Thursday, October 5, 2022
#                |
#    Description | This program asks the user how many Air Canada points they have,
#                | then applies a bonus based on the entered amount. Program will
#                | continue to run until user indicates they would like to leave.


# Start while loop allowing user to continue or exit the program
while True:

    # Display title 
    print("{:-^80}".format("Air Canada Aeroplan Miles Customer Service"))

    # Display introductory paragraph
    print("\nThis program functions as the Air Canada Aeroplan Miles Customer Service! It")
    print("will calculate and apply bonus points based on the current standing of your")
    print("points. Please follow all instructions.")

    # Start while loop in case user enters invalid value
    while True:    
        # Asks user to enter current amount of points
        points=int(input("\nEnter '0' for points to exit. Enter current number of points: "))

        # If points are not greater than or equal to 0 display error message
        if (points>=0):
            break
        print("Error! Enter a value that is 0 or greater.")
    
    # If user enters 0 for points exit the program
    if (points==0):
        break
    
    # If points are between 1 and 4999
    # Store bonus points as 250
    if (points>=1 and points<=4999):
        bonusPts=250
    
    # Else if points are between 5000 and 9999
    # Store bonus points as 500
    elif (points<=5000 and points>=9999):
        bonusPts=500
    
    # Under any other condition 
    # Store bonus points as 750
    else:
        bonusPts=750
    
    # Display point information
    print("\n{:17} {:8d}".format("Current points:",points))
    print("\n{:17} {:8d}".format("Bonus points:",bonusPts))
    
    # Calculate total points
    totalPts=points+bonusPts
    print("\n{:17} {:8d}\n".format("Total Points:",totalPts))

# Display parting message
print("\nCome again, thanks for using Air Canada Aeroplan Miles Customer Service!")








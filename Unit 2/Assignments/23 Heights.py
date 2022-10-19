#     Assignment | Assignment 2-3
#  Program Title | Class Average Heights
#                |
#     Written by | Khurram Shaikh
#           Date | Wednesday, October 19, 2022
#                |
#    Description | This program asks for the heights of students in 
#                | a class, then displays the class's average height
#                | to one decimal place. Program continues to run 
#                | until user exits, displays total classes.

classes=0

# Start infinite loop
while True: 
    sum=0
    print("{:*^80s}".format("Class Average Height Calculator"))
    
    # Start infinite loop in case user enters invalid value
    while True:
        
        # Ask for amount of students
        students=int(input("Enter amount of students ('0' to exit): "))
        
        # If amount is a negative number display error message
        if (students>=0):
             break
        print("Error invalid student amount, enter a positive value!")
    
    # If amount is equal to 0 exit program
    if (students==0):
        break
    classes+=1
    
    # Display prompt for height
    print("\nEnter height:")
    
    # Start counted loop to total amount of students
    for x in range(students):
        
        # Start infinite loop in case user enters invalid value
        while True:
            
            # Ask user for height
            height=float(input(""))

            # If height is less than 150 and greater than 220 
            # display error message
            if (height>=150 and height<=220):
                break
            print("Error invalid height, enter a value between 150 and 220!")
        
        # Add height and store in sum
        sum+=height
    
    # Calculate average
    avg=sum/students
    
    # Display average height to one decimal place
    print("Average height is: {:.1f} cm".format(avg),end=" ")
    
    # If classes are greater than 1 display total classes 
    if (classes>1):
        print("and a total of {} classes.".format(classes))    
    
    # Start while loop 
    while True:
        restart=input("\nWould you like calculate the average height again? Enter 'y' or 'n': ")
        
        # If user enter's an invalid value 
        # display error message
        if (restart=='n' or restart=='y'):
            break
        print("Error invalid response, enter 'y' or 'n'.")
    
    # If user enter's 'n' exit program
    if (restart=='n'):
        break
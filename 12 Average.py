#     Assignment | Assignment 1-2 
#  Program Title | The Average Calculator
#                |
#     Written by | Khurram Shaikh
#           Date | Friday, September 23, 2022
#                |
#    Description | This program asks for the user's name, four valid marks from last semester,
#                | and then displays their cumulative average to one decimal place.
#                | Advice is provided based on mark standing, the program will continue 
#                | until user exits. 

# Start while loop allowing user to continue or exit the program
while True: 
     
    # Ask user if they would like to start/continue program
    exit_prog=input("\n'Yes/Y' to continue/start program, 'No/N' to exit: ")
    
    # If user enters N or No, exit the program
    if(exit_prog=="N" or exit_prog=="No"):
        break
    
    # Else if user enters Y or Yes, continue the program
    elif(exit_prog=="Y" or exit_prog=="Yes"):
        print()
        print('{:*^80s}\n'.format("The Average Calculator"))
        
        # Display welcome message and instructions
        print("Hello! Please follow all instructions. This program will calculate your average")
        print("for last semester, from your four marks. Advice will also be provided based on")
        print("average! Please enter marks as whole numbers.\n")

        # Ask user to enter their name
        name=input("Please [ENTER] your name: ")

        # Starts while loop in case user enters invalid value
        while True:

            # Ask user to enter four whole number marks from last semester
            mark1,mark2,mark3,mark4=int(input("\n[ENTER] first mark from course #1: ")),int(input("\n[ENTER] second mark from course #2: ")),int(input("\n[ENTER] third mark from course #3: ")),int(input("\n[ENTER] fourth mark from course #4: "))
        
            # If marks are greater than 100 or less than 0 tell user to enter valid value
            if (mark1<=100 and mark2<=100 and mark3<=100 and mark4<=100 and mark1>=0 and mark2>=0 and mark3>=0 and mark4>=0):
                break
            print("\nError! Please enter a valid value no greater than 100 and no less than 0.")   
        
        # Creates an array of four marks 
        listOf_marks=[mark1,mark2,mark3,mark4]
        print()
        
        # Divides the sum of the array with the total items in the array 
        mrkAvg=sum(listOf_marks)/len(listOf_marks)

        # Displays user's name and final average last semester to one decimal place
        print("{}, your average for last semester was: {:.1f}%.".format(name,mrkAvg))

        # If average is greater than or equal to 90 notify the user that they did a good job
        if (mrkAvg>=90):
            print("\nNice! Good work, last semester your average was greater than 90%.")
            print('{:-^80s}'.format(""))

        # If average is greater than or equal to 75 notify the user that they can do better to go above and beyond
        elif (mrkAvg>=75):
            print("\nYou scored an average greater than 75%! Put in more effort, time and interest to go above and beyond.")
            print('{:-^80s}'.format(""))
        
        # In any other condition notify the user that mistakes are fine and it is encouraged that they improve
        else:
            print("\nMistakes are a way to learn! Highly encouraged for you to try harder and improve this term.")
            print('{:-^80s}'.format(""))


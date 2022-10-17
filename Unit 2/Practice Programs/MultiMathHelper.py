# 10 Practice Programs 2
# Program 6: Multi Math Helper
#
# Khurram Shaikh
# Friday, October 14, 2022
#
# This program asks the user for a number,
# and then displays the multiplication table 
# through 10.

# Start infinite loop
while True:
    
    # Ask user to enter a number 
    number=int(input("Enter number for multiplication table ('0' to exit): "))
    
    # If number is 0 exit loop
    if (number==0):
        break
    
    # Start counted loop from 1 to 10
    for x in range(1,11):
        
        # Display multiplication table
        # Multiply loop amount by user number 
        print("{:<4d} X {:4} = {:6}".format(number,x,number*x))

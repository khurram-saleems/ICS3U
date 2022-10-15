# 07 How many friends?
# 
# Khurram Shaikh
# Friday, October 7, 2022
#
# This program starts a loop and asks the user to enter the 
# name of their friend(s). Once the user wants to stop,
# the count of friends is displayed.

# Initialize count to 0
count=0

# Start infinite loop
while True:
    
    # Ask user to enter friend name 
    friends=input("Type 'STOP' to end loop. Enter friend's name: ")
    
    # If user wants to stop exit loop
    if (friends=="STOP"):
        break

    # Add one to count
    count+=1

# Display count of friends
print("You have {} friends.".format(count))
#     Assignment | Assignment 3-1
#  Program Title | Shrinking Sentence 
#                |
#     Written by | Khurram Shaikh
#           Date | Wednesday, November 2, 2022
#                |
#    Description | 

# Start infinite loop
while True:
    space=""
    
    # Start infinite loop in case user enters invalid value
    while True:
        
        # Ask user for sentence 
        sentence=input("Enter a sentence:\n")[0].upper()
        
        # If length of sentence is less than 5 
        # Display error message
        if (len(sentence)>=5 and sentence[-1]=='.'):
            break
        print("Error, invalid value! Enter a sentence with 5 characters and correct punctuation.")
    print()
    
    # Start counted loop from length of sentence to 0
    # 
    for x in reversed(range(0,len(sentence)+1)):
        print(sentence[:x])
    print()
    for x in range(0,len(sentence)):
        print(space+sentence[x:])
        space+=" "
    while True:
        exitOrRun=input("Would you like to try again? Enter 'y' or 'n'. ")
        if (exitOrRun=='y' or exitOrRun=='n'):
            break
        print("Error! Enter 'y' or 'n'.")
    if (exitOrRun=='n'):
        break
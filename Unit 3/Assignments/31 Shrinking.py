#     Assignment | Assignment 3-1
#  Program Title | Shrinking Sentence 
#                |
#     Written by | Khurram Shaikh
#           Date | Wednesday, November 2, 2022
#                |
#    Description | This program ask the user to enter a sentence,
#                | then displays it with shrunken characters from
#                | the end and beginning. Program continues to
#                | run until user exits, and user must enter 
#                | correct punctuation.

# Set punctuation as period, exclamation mark and question mark
punctuation=('.','!','?')

# Start infinite loop
while True:
    space=""
    
    # Start infinite loop in case user enters invalid value
    while True: 
        
        # Ask user for sentence 
        sentence=input("Enter a sentence:\n")
        
        # If length of sentence is less than 5, first character
        # isn't capitalized and ending punctuation is incorrect 
        # Display error message
        if (len(sentence)>=5 and sentence[0].isupper() and sentence.endswith(punctuation)):
            break
        print("Error, invalid value! Enter a sentence with at least 5 characters and correct punctuation.")
    print()
    
    # Start counted loop from length of sentence to 0
    # Display sentence to counted character
    for x in reversed(range(0,len(sentence)+1)):
        print(sentence[:x])
    
    # Start counted loop from 0 to length of sentence
    # Display space and counted character of sentence to end
    for x in range(0,len(sentence)):
        print(space+sentence[x:])
        space+=" "
    
    # Start infinite loop in case user enters invalid value
    while True:
        
        # Ask if user would like to try again
        exitOrRun=input("Would you like to try again? Enter 'y' or 'n'. ")[0].lower()
        
        # If user does not enter 'y' or 'n'
        # Display error message
        if (exitOrRun=='y' or exitOrRun=='n'):
            break
        print("Error! Enter 'y' or 'n'.")
    
    # If user enters 'n' exit program
    if (exitOrRun=='n'):
        break

# Display parting message
print("\nThanks for using The Sentence Shrinker, come again!")
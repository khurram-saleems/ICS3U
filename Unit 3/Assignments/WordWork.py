#     Assignment | Assignment 3-2
#  Program Title | The Word Food Processor 
#                |
#     Written by | Khurram Shaikh
#           Date | Tuesday, November 14, 2022
#                |
#    Description | This programs asks the user to enter a sentence
#                | and then provides various options to manipulate.
#                | Program continues to run until user exits.

import random

# Ask user for string
sentence=input("\nEnter a sentence: ")
    
while True:

    # Display prompt for option
    print("\nChoose an option:")
    print("1 - display sentence in reverse order")
    print("2 - display only the vowels")
    print("3 - display only the consonants")
    print("4 - sentence validator")
    print("5 - word count")
    print("6 - scramble sentence")
    print("7 - enter a new sentence")
    print("8 - exit")

    # Start infinite loop in case user enters invalid value
    while True:
        
        # Ask for option
        option=int(input())
        if (option>=1 and option<=8):
            break
        print("Error! Enter an available option.")
    
    # If option is 1 display reverse order of string
    if (option==1):
        for i in reversed(range(len(sentence))):
            print(sentence[i],end="")
    
    # Else if option is 2 display vowels
    elif (option==2):
        vowels=('AaEeIiOoUu')   
        for i in range(len(sentence)):
            character=vowels.find(sentence[i])
            if (character>=1):
                print(vowels[character],end="")
    
    # Else if option is 3 display consonants 
    elif (option==3):
        consonants=('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
        for i in range(len(sentence)):
            character=consonants.find(sentence[i])
            if (character>=1):
                print(vowels[character],end="")
    
    # Else if option is 4 verify if sentence is gramatically correct
    elif(option==4):
        punctuation=('.','!','?')
        if (sentence[0].isupper()):
            print("Sentence starts with a capital.")
        elif (sentence.endswith(punctuation)):
            print("Your sentence ends with a correct piece of punctuation: {}".format(sentence[-1]))
        elif (sentence[0].isupper() and sentence.endswith(punctuation)):
            print("Satisfies the criteria of a sentence.")
        else:
            print("This is not a sentence.")
    
    # Else if option is 5 display word count of sentence
    elif (option==5):
        print("Word count of sentence is: {}".format(sentence.count(" ")+1))
    
    # Else if option is 6 scramble sentence
    elif (option==6):
        for i in range(len(sentence)):
            r=random.randint(0,len(sentence)-2)
            print(sentence[r],end="")
    elif (option==7):
        # Ask user for string
        sentence=input("\nEnter a sentence: ")
    else:
        print("Thanks for using the Word Food Processor")
        break
        


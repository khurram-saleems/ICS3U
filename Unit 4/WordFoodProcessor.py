# Assignment 3-2 
# Word Food Processor 
# 
# Written by Mr. Milardovic 
# Thursday, November 14, 2019 
# 
# This program demonstrates different ways to manipulate a sentence. 
# get the user's sentence 

text=input("Enter a sentence\n") 
while True: 

    # display the title 
    print() 
    print() 
    print("The Word Food Processor") 
    print("=======================") 
    print() 

    # display the menu 
    print("Choose an option:") 
    print("1 - display sentence in reverse order") 
    print("2 - display only the vowels") 
    print("3 - display only the consonants") 
    print("4 – sentence validator") 
    print("5 - enter a new sentence") 
    print("6 - quit") 
    print() 

    # error trap user's choice 
    while True: 
        choice=int(input("Enter choice: ")) 
        if (choice>=1 and choice <=6): 
            break 
        print("That is not a valid choice") 
    if (choice==1): 

        # display the sentence in reverse 
        for i in reversed(range(len(text))): 
            print(text[i],end="") 
        print() 
    elif (choice==2):

        # declare string of vowels 
        vowels="aeiouAEIOU" 

        # go through characters of text one at a time checking if each is 
        # found in my string of vowels. 
        for i in range(len(text)): 
            if(vowels.find(text[i])>-1): 
                print(text[i],end="") 
        print() 
    elif (choice==3): 
        
        # declare string of consonants 
        consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" 

        # go through characters of text one at a time checking if each is 
        # found in my string of vowels. 
        for i in range(len(text)): 
            if(consonants.find(text[i])>-1): 
                print(text[i],end="") 
        print() 
    elif (choice==4): 
        # verify that what the user entered is a sentence 
        if (text[0].isupper() and (text.endswith(".") or text.endswith("!") or text.endswith("?"))): 
            print("This is a proper sentence.") 
        else: 
            print("Not a proper sentence. ",end="") 
            if (text[0].isupper()==False): 
                print("It doesn't start with a capital. ",end="") 
            if (not (text.endswith(".") or text.endswith("!") or text.endswith("?"))): 
                print("It doesn't end with proper punctuation.",end="")
            print() 
    elif (choice==5): 
        # get a new sentence 
        text=input("Enter a sentence\n") 
    else: 
        break 
# Assignment 3-2 
# Word Food Processor 
# 
# Written by Mr. Milardovic 
# Thursday, November 14, 2019 
# 
# This program demonstrates different ways to manipulate a sentence. 
# get the user's sentence 

def validVal(x,y):
    """Ask the user for a number between two
    given numbers, and return the value.

    Arguments:
        x: starting number to check between.
        y: ending number to check between.

    Returns:
        Valid number between arguments.
    """
    while True:
        v=int(input("Enter a value: "))
        if (v>=x and v<=y):
            break
        print('error')
    return v

def newSent():
    """Asks and returns user's sentence. 

    Returns: 
        User's sentence
    """
    text=input("Enter a sentence\n")
    return text

def validateSent(text):
    """Validates if sentence has correct punctuation,
    given text.

    Arguments:
        text: The data to validate.
    """
    if (text[0].isupper() and (text.endswith(".") or text.endswith("!") or text.endswith("?"))): 
            print("This is a proper sentence.") 
    else: 
        print("Not a proper sentence. ",end="") 
        if (text[0].isupper()==False): 
            print("It doesn't start with a capital. ",end="") 
        if (not (text.endswith(".") or text.endswith("!") or text.endswith("?"))): 
            print("It doesn't end with proper punctuation.",end="")

def showCons(text):
    """Display consonants of sentence, given text.

    Arguments:
        text: The data to display consonants of.
    """
    consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" 
    for i in range(len(text)): 
        if(consonants.find(text[i])>-1): 
            print(text[i],end="")

def showVowels(text):
    """Display vowels of sentence, given text.

    Arguments:
        text: The data to display the volwels of.
    """
    vowels="aeiouAEIOU" 
    for i in range(len(text)): 
        if(vowels.find(text[i])>-1): 
            print(text[i],end="") 

def reverse(text):
    """Display the sentence reversed, given text.
    
    Arguments:
        text: The data to reverse.
    """
    for i in reversed(range(len(text))): 
            print(text[i],end="") 
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
    print("4 - sentence validator") 
    print("5 - enter a new sentence") 
    print("6 - quit") 
    print() 
    choice=validVal(1,5)
    print(choice)
    if (choice==1): 
        reverse(text)
        print() 
    elif (choice==2):
        showVowels(text)
        print() 
    elif (choice==3): 
        showCons(text)
        print() 
    elif (choice==4): 
        validateSent(text)
        print() 
    elif (choice==5): 
        text=newSent()
    else: 
        break 
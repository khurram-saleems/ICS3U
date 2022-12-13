# Command Finder  

# Assighnment 5-1  

  

# Somai Umair  

# Friday, December 9  

  

# This program will help the user find the  

# command with the file  

  

  

# function  

def findCommand(fileName, command):  

  

    """ finds where the command is found, then displays  

        the lines it is used in. It also counts up how  

        many times the command was in the file, including comments.  

  

        Arguments: 

        file name -- Takes in the file name  

        command -- takes in the command given  

  

""" 

    # Initialize 

    count = 0 

    numComment = 0 

    numLines = 0 

  

    # Open the file 

    file = open(fileName,"r")  

  

    # If statements ensuring different situation 

    while True:  

        rLine = file.readline()  

        if (rLine == ""):   

            break 

  

        numLines += 1  

  

        if (rLine.find(command) > -1):  

            print("({:1})     {}" .format( numLines,rLine.strip())) 

            count += 1 

  

        if (rLine.strip().startswith("#")): 

            numComment += 1 

  

    file.close() 

  

    print() 

      

    # Ensures when what needs to be displayed 

    if (count > 0): 

        print("{} lines had the command".format(count)) 

  

    else: 

        print("command was not found") 

     

    print() 

  

    # Ensures 'Enter' is pressed(Not Workng) 

    if (numLines == 20 ): 

        input("'Enter' to continue: ") 

        print("({:1})     {}" .format( numLines,rLine.strip())) 

  

  

    print("lines with the command as comments are {}" .format(numComment)) 

  

# # # # # MAIN PROGRAM # # # # #  

  

# Title  

print("Somai's file command finder")  

  

print()  

  

# File name with .py  

fileName = input("Enter file name: ")  

if (fileName .endswith(".py") == False):   

    fileName += ".py"  

  

print()  

  

# Command user wants   

command = input("Enter a python command: ")  
print()  

# Calling the function   
findCommand(fileName, command)
#     Assignment | Assignment 5-1
#  Program Title | Command Finder
#                |
#     Written by | Khurram Shaikh
#           Date | Friday, December 9, 2022
#                |
#    Description | This program asks the user to enter the name of a Python
#                | file and a command within the file, it then proceeds to 
#                | search for occurences of that command and displays
#                | information related to a file, in a report-like format.

def findCommand(fileName,command):
    """Searches through a file and displays lines
    of the program that contain the command.

    Arguments:
        fileName: Name of file that the user enters.
        command: Command that the file is being searched for.
    """
    lineCount,commandCount,commentCount=0,0,0
    fin=open(fileName,"r")
    while True: 
        if (commandCount%20==0 and commandCount!=0):
            input("[ENTER] to continue: ")
        line=fin.readline()
        if line=="":
            break
        lineCount+=1
        if line.strip().find(command)!=-1 and line.strip().startswith("#")==False:
            commandCount+=1
            print("({:3d})      {}".format(lineCount,line.strip()))
        if line.strip().startswith("#") and line.strip().find(command)!=-1:
                commentCount+=1
    fin.close()
    print("\nInformation for {}".format(fileName))
    print("{:21s} {:3d}.".format("Line count:",lineCount))
    print("{:21s} {:3d}.".format("Comment line count:",commentCount))
    if (commandCount==0):
        print("{} was not found in {}.".format(command,fileName))
    else: 
        print("'{}' was found {} times in {}".format(command,commandCount,fileName))

import os.path

### MAIN PROGRAM ###

print("{:•^80s}".format("2022 Command Finder by ClosedAI"))

# Start infinite loop
while True: 
    
    # Start infinite loop in case user enters invalid value
    while True: 
    
    # Ask user to enter filename
        fileName=input("Enter a Python filename: ")
    
        # If filename does not end with '.py' extension add it
        if (fileName.endswith(".py")==False):
            fileName+=".py"
        
        # If file does not exist display erorr message
        if (os.path.exists(fileName)):
            break
        print("\nError, invalid filename! Enter the name of a file which exists.")
    
    # Ask user for command
    command=input("Enter the command you are searching for: ")
    
    # Call function to search through file and display lines 
    # which contain command
    findCommand(fileName,command)
    
    # Start infinite loop
    while True:
        
        # Ask if user would like to search again
        newProgram=input("\nWould you like to search for something else ('y' or 'n')? ")
        
        # If user does not enter 'y' or 'n'
        # Display error message
        if (newProgram=='y' or newProgram=='n'):
            break
        print("\nError, enter 'y' or 'n'.")
    
    # If user enters 'n' exit program
    if (newProgram=='n'):
        break
print("Thanks for using the Command Finder!")
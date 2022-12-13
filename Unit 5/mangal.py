# commandFinder
#
# Mangalpreet Singh
# December 9, 2022
#
# Find the command in file entered by user.



def findCommand(fileName, command):
    """Find if command exists inside of file.
    If command exists, tell user the line
    of code and what line its at. Count the
    total lines, and comment lines in code.
    Tell user the count.

    Arguments:
    

    Returns: 

    """
    
    Linecount=0
    numFindLine=0
    numCommLine=0
    fout= open(fileName, "r")
    while True:
        if numFindLine==20:
            clearScreen= input("Press enter: ")
            print("/n"*10)
        
        line= fout.readline()
        if line=="":
            break
        Linecount+=1
        if line.strip().find(command)>=0:
            print("({})    {}".format(Linecount, line.strip()))
            numFindLine+=1
        if line.strip().startswith("#"):
            numCommLine+=1
        
    fout.close()
    print("You had {} lines in code.".format(Linecount))
    if numFindLine==0:
        print("No {} lines were found in the code...".format(command))
    else:
        print("You had {} {} command lines".format(numFindLine, command))
    print("You had {} comment lines".format(numCommLine))

###MAIN###

# Tell user the title
print("Welcome to Mangal's Command Finder!")


# Put program in loop
while True:
    # Ask user for the file name
    fileName= input("Enter file name: ")

    # Add .py to file name if user did not add it.
    if (fileName.endswith(".py")==False):
        fileName+=".py"
    
    # Ask user the command to find
    command= input("Enter the command: ")


    # Call findCommand and pass the fileName and command into it.
    findCommand(fileName, command)


    # Infinite loop for error trapping
    while True:
        # Ask user if they would like to restart the program
        userRestart= input("Would you like to enter a new command? y/n: ")

        # Error trapp the user's input
        if userRestart=="y" or "n":
            break
        print("Invalid Response....")

    # Exit program if user says n
    if userRestart=="n":
        print("Thank you for trying.")
        break
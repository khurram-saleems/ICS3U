# Friends IO 2.0
#
# Khurram Shaikh
# Thursday, December 15, 2022
#
# This program experiments with File IO,
# asks user to select option from a menu
# to to make changes to the file.

def getFileName():
    """Asks the user for a filename,
    ensures it is able to be opened.

    Returns:
        Valid name of file.
    """ 
    
    # Start infinite loop 
    while True:
        
        # Ask user for file name 
        fName=input("Enter file name: ")
        
        # Call function to check if file exists 
        # Set boolean to found
        found=checkFileExist(fName)
        
        # If found is False or filename is not blank
        # Display error message
        if (found==True or fName==""):
            break
        print("Error, file does not exist.")
    
    # If filename is blank change it to 'friends.txt'
    if (fName==""):
        fName="friends.txt"
    
    # If it does not end with '.txt'
    # Add the correct extension
    if (fName.endswith(".txt")==False):
        fName+=".txt"
    return fName

def writeNames(fName):
    """Writes to a file, asks user to enter friends names,
    and exits when user wants.

    Arguments:
        fName: Name of file.
    """

    # Open file to write 
    fout=open(fName,"w")
    
    # Start infinite loop
    while True:
        # Ask user to enter friend's name
        print("Enter a friend's name ('STOP' to stop):")
        name=input("-> ")
        
        # If user enter's stop exit loop
        if (name=="STOP"):
            break
        
        # Write friend's name to file
        fout.write(name+"\n")
    
    # Close the file 
    fout.close()

def readNames(fName):
    """Reads from a file, displays friends and a number beside 
    each one, pauses after twenty friends.

    Arguments:
        fName: Name of file.
    """
    
    # Open file for reading
    fin=open(fName,"r")
    
    # Set friendCount to 0
    friendCount=0
    
    # Start inifinite loop
    while True:
        
        # Set line to line from file object
        line=fin.readline().strip()
        if line=="":
            break
        # Add one to count of friends
        friendCount+=1
        
        # Display count of friends and current line
        print(friendCount,line)

        # If it has been 20 friends pause
        if (friendCount%20==0):
            input("[ENTER] to continue: ")
    
    # Close file
    fin.close()

def validVal(x,y):
    """Ask user for an option between given parameters,
    returns the valid value.

    Arguments:
        x: lowest value to check between.
        y: highest value to check between.
    
    Returns:
        Valid option between arguments.
    """
    
    # Start infinite loop in case user enters invalid value
    while True:
        
        # Ask user for option 
        option=int(input("Enter an option between {} and {}: ".format(x,y)))
        
        # If option is not between given parameters
        # Display error message
        if (x<=option<=y):
            break
        print("Error, enter an option between {} and {}!".format(x,y))
    return option

def checkFileExist(fileName):
    """Returns True or False on the existence of a given
    file.

    Arguments:
        fileName: Name of file to check existence of.
    
    Returns:
        True or false, boolean value of if the file exists.
    """
    return os.path.exists(fileName)

def searchFriend(fileName):
    """Search given file for data, displays message based 
    on whether it exists within file.

    Arguments:
        fileName: Name of file to check data in.
    """
    
    # Ask for name to search for
    searchName=input("Enter name to search for: ")
    
    # Set found to false
    found=False
    
    # Open file to read from
    searchFin=open(fileName,"r")
    
    # Start infinite loop
    while True:
        
        # Set line to line from file object
        line=searchFin.readline().strip()
        if line=="":
            break
        
        # If searched name is line 
        if searchName==line:
            
            # Set found to True
            found=True
    
    # Close file
    searchFin.close()
    
    # If found is True notify user that data exists
    if found==True:
        print("Name exists within file.")
    
    # Else notify user that data does not exist within file
    else:
        print("Name does not exist within the file.")

def addToFile(fileName):
    """Adds to file, asks user for name of friend to add
    to given file.

    Arguments:
        fileName: Name of file to append to.
    """
    
    # Open file to append 
    fout=open(fileName,"a")
    
    # Start infinite loop
    while True:
        
        # Ask user for friend's name
        print("Enter a friend's name ('STOP' to stop):")
        name=input("-> ")
        
        # If user enter's 'STOP' exit loop
        if (name=="STOP"):
            break
        
        # Add friend's name to file
        fout.write(name+"\n")
    
    # Close file
    fout.close()

def deleteFromFile(fileName):
    """Deletes data from file, give file name.

    Arguments:
        fileName: file to delete data from.
    """
    dataRemove=input("Enter data to delete: ")
    fin=open(fileName,"r")
    fout=open("temp.txt","w")
    while True:
        name=fin.readline().strip()
        if name=="":
            break
        if name!=dataRemove:
            print(name,file=fout)
    fin.close()
    fout.close()
    os.remove(fileName)
    os.rename("temp.txt",fileName)

import os

# Start infinite loop 
while True:
    
    # Call function to get file name
    fileName=getFileName()
    
    # Display options
    print("\nOption 1 - Write Friend names")
    print("Option 2 - Read Friend Names")
    print("Option 3 - Search File For A Person")
    print("Option 4 - Add To File")
    print("Option 5 - Delete From File")
    print("Option 6 - Exit Program\n")
    
    # Call function to ask user for a valid option
    option=validVal(1,6)
    
    # If option is one 
    if (option==1):
        
        # Call function to write to file
        writeNames(fileName)
    
    # Else if option is two 
    elif(option==2):
        
        # Call function to read from file
        readNames(fileName)
    
    # Else if option is three  
    elif(option==3):
        
        # Call function to search file
        searchFriend(fileName)
    
    # Else if option is four 
    elif(option==4):
        
        # Call function to append to file
        addToFile(fileName)
    
    # Else if option is five
    elif(option==5):
        
        # Call function to delete data from file
        deleteFromFile(fileName)
    
    # Else display parting message and exit program 
    else:
        print("Goodbye.")
        break
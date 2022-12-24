def validVal (number1,number2): 
    """Ensures the user has inputted a value that is range of two numbers.
    Arguments:
    number1: This value will be the lowest number limit 
    number2: This value will be the highest number limit 
"""
    # Start error loop, ensure values are between 1 and 2
    while True: 
        option = int(input("Choose an option: ")) 
        if option >= number1 and option <=  number2: 
            break 
        print ("invalid") 

        # return the proper value
    return option

# Asks user for list name
def nameOfList():
    """ Asks the user for a list name, it sets listName to 
        'Presents.txt' if left blank. It also checks if 
        listName ends with '.txt', adds it if not found.

        Returns:
        -- The provided list name accuratley
"""
    # Ask user for list name
    listName = input("Name of the list (Press 'ENTER' to skip): \n")

    # If user leaves blank, listName is set to 'Presents.txt'
    if (listName == ""):
        listName = "presents.txt"

    # Ensures if users has added .txt, adds it if not found.
    if (listName.endswith(".txt") == False):
        listName += ".txt"

    # Returns the list name
    return listName

def writeList(listName):
    """" Writes to a file given, takes the
        name, present, and store and adds
        it to the file.

         Arguments:
         listName -- The file name
""" 
    # Opens file to writing 
    Fout = open(listName, "w" )

     # loop starts 
    while True: 

        # ask for friends name
        frndName = input("Enter Name ('STOP' to exit): ")

        # checks if user has inputted 'STOP'
        if (frndName == "STOP"):
            break

        # Ask for frndsPresent
        frndsPresent = input("Enter there present: ")

        # asks for presentStore
        presentStore = input("Enter the store: ")

        # Write to the file
        Fout.write("Name: {:10} Present: {:10} Store: {:10}\n".format(frndName,frndsPresent,presentStore))

    # close file
    Fout.close()

def readList(listName):
    """ Reads from the file given, counts each item that has
        been given and displays it.

    Arguments:
    listName-- name of file.
"""
    # Setting itemCount to 0    
    itemCount = 0

        # Opens file given to read.
    Fin = open(listName, "r") 

    # Start loop
    while True:  

        # Read each line
        rLine = Fin.readline() 

        # If line is blank, exit
        if (rLine == ""): 
            break 
        itemCount += 1

        # display the line
        print("{}" .format( rLine.strip()))

        print()
    
    # ask user to press enter
    input("Press 'ENTER' to continue: ")

    # display number of items
    print("Number of items: {}".format(itemCount))
        
    # close the file 
    Fin.close()

def addToFile(ListName):
    """ Appends the name given to the file given.

    Arguments:
    listName -- Name of file 
    """
    
    # Open file to append 
    fout = open(ListName,"a")
    
    # Start loop 
    while True:
    
        aName = input("Enter a friend's name ('STOP' to exit): ").upper()
        
        if (aName == "STOP"):
            break

        print()

        aPresent = input("Enter a present: ")

        print()

        aStore = input("Enter Store: ")

        print()

        # Add name to file
        fout.write("Name: {:10} Present: {:10} Store: {:10}" .format(aName, aPresent,aStore))
    
    # Close file
    fout.close()

def deleteData (listName):
    """ Deletes people, peoples present, presents website 
        from given file.

        Arguments:
        listName -- The accurate file name
"""
    # Asks what needs to be deleted
    nameDelete = input("Name to delete: ")

    # Ask if all has to be deleted or specific
    allOrSpecific = input("Would you like to delete a specific present or every present? ('specific' or 'all'): ")

    # open file to read
    fin = open(listName, "r")

    # open temporary file
    fout = open ("temp.txt","w")

    # start loop
    while True: 

        # Read through file 
        data = fin.readline()
         
        # If line is blank exit
        if (data==""):
            break
        if (data.strip().find(nameDelete)!=-1):
            
            # checks if allOrSpecific is 'specific'
            if (allOrSpecific == "specific"):

                # ask if user is sure
                yesNo = input("Are you sure you want to delete {}'s present a {}('yes' or 'no'): ".format(nameDelete, data))

                # if the yesNo is 'no'
                if (yesNo == "no"): 
                    # display 
                    print(data.strip(), file=fout)
        else:
            print(data.strip(), file=fout)
    
    fout.close()
    fin.close()

    os.remove(listName)
    os.rename("temp.txt",listName )


# # # # # # MAIN PROGRAM # # # # # # # 
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # #


import os

print()

while True:

    # Display options
    print("1 - Write a list")
    print("2 - Read the list")
    print("3 - Add to a list")
    print("4 - Delete data in list")
    print("5 - search")
    print("6 - Exit Program")

    # Call function to ask user for a valid option
    option = validVal(1,7)

    fileName = nameOfList()

    # if option is 1
    if (option == 1):

        # call function
        writeList(fileName)

    # if option is 2
    elif(option == 2):

        # Call the function
        readList(fileName)

    # If option is 3
    elif(option == 3):

        # call the function
        addToFile(fileName)

    # if option is 4
    elif(option == 4):

        # call the function
        deleteData(fileName)
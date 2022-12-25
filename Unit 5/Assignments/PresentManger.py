#     Assignment | Assignment 5-2
#  Program Title | The Present Manager
#                |
#     Written by | Khurram Shaikh
#           Date | Thursday, December 22, 2022
#                |
#    Description | This program manages a list of gift recipients 
#                | and the gifts that need to be purchased for 
#                | them. It allows users to create a new list, 
#                | add to the list, read from the list, and 
#                | delete items from the list. The list is stored 
#                | in a text file and consists of the recipient's 
#                | name, the gift to be purchased, and the store 
#                | where the gift can be purchased. 

def createNewList(listName):
    """Creates a new gift list with the given name.
    If the list already exists, the user is prompted 
    to delete the existing content.

    Arguments:
        listName: Name of the gift list to create.
    """
    
    # Call function to get line count
    lineCount=getLineCount(listName)
    
    # If line count greater than 0 
    # Notify user that file contains existing content
    if (lineCount>0):
        delete=getYOrN("File contains existing content, delete and write ('y' or 'n')? ")
        
        # If user does not want to delete and write
        # Return to main menu
        if (delete=="n"):
            pressEnter()
            return
    
    # Open list to write 
    fout=open(listName,"w")
    lineCount=0
    
    # Start infinite loop 
    while True:
        
        # Ask user for name and exit loop 
        name=input("Enter name (blank to exit): ")
        
        # If name is blank exit loop
        if (name==""):
            break
        
        # Ask for present to purchase
        present=input("Enter gift to purchase: ")
        
        # Ask for store to purchase
        store=input("Enter store where product is available: ")
        
        # Write name, present and store to the list
        fout.write("{:20.20s} {:30.30s} {:20.20s}\n".format(name,present,store))
        lineCount+=1
    
    # Close the file
    fout.close()
    
    # If line count is not 0
    # Display total items after writing
    if (lineCount!=0):
        print("After writing: total of {} item".format(lineCount),end="")
        if (lineCount>1):
            print("s!")
    pressEnter()

def readFromList(listName):
    """Reads the gift list with the given name and
    displays the content.

    Arguments:
        listName: Name of the gift list to read.
    """
    
    # Call function to get line count
    lineCount=getLineCount(listName)
    
    # If line count greater than 0 
    # Notify user that file contains existing content
    if (lineCount==0):
        print("No items within the list.")
    
    # Else read from file
    else:
        with open(listName,"r") as fin:
            lineCount=0
            print("\n{:>3s}  {:20} {:30} {:20}".format("Num","Name","Gift","Store"))
            
            # Start infinite loop
            while True:
                
                # Read a line from file
                recipientInfo=fin.readline()
                
                # If line is blank exit loop
                if (recipientInfo==""):
                    break
                lineCount+=1
                
                # Display recipient info 
                print("{:3}. {}".format(lineCount,recipientInfo.strip()))
                
                # If it has been an iteration of 20 lines
                if (lineCount%20==0):
                    # Call function to pause screen
                    pressEnter()
            
            #Display total items after reading
            print("After displaying: total of {} item".format(lineCount),end="")
            if (lineCount>1):
                print("s!")
    pressEnter()

def addToList(listName):
    """Adds a new entry to the gift list with
    the given name.

    Arguments:
        listName: Name of the gift list to add to.
    """
    
    # Open file to append
    fout=open(listName,"a")
    
    # Start infinite loop
    while True:
        
        # Ask user for name
        name=input("Enter name (blank to exit): ")
        
        # If name is blank exit loop
        if (name==""):
            break

        # Ask for present
        present=input("Enter gift to purchase: ")
        
        # Ask for store 
        store=input("Enter store where product is available: ")
        
        # Write name, present and store to the list
        fout.write("{:20.20s} {:30.30s} {:20.20s}\n".format(name,present,store))
    
    # Close file 
    fout.close()
    
    # Call function to get line count
    lineCount=getLineCount(listName)
    
    # If line count is not 0
    # Display total items after writing
    if (lineCount!=0):
        print("After adding to list: total of {} item".format(lineCount),end="")
        if (lineCount>1):
            print("s!")
    pressEnter()

def deleteFromList(listName):
    """Deletes all or selective items
    from a list of presents.

    Arguments: 
        listName: The name of file containing the list of presents.
    """
    
    # Call function to get line count
    lineCount=getLineCount(listName)
    
    # If line count is 0 notify that there are no items within list
    if (lineCount==0):
        print("No items within the list.")
    
    # Else delete from list
    else:
        
        # Ask for name to delete items for
        nameRmve=input("Enter name to delete items for: ")
        
        # Ask to delete all items or specific
        allOrSelect=input("'A'll items or 'S'elective? ").upper()
        
        # Open file to read
        fin=open(listName,"r")
        
        # Open temporary file to write
        fout=open("temp.txt","w")
        deleteCount=0
        
        # Start infinite loop
        while True:
            
            # Read line from the list
            recipientInfo=fin.readline()
            if (recipientInfo==""):
                break
            
            # If name to remove is in line
            if (recipientInfo.strip().find(nameRmve)!=-1):
                
                # If user would like specific items to be deleted
                if (allOrSelect=="S"):
                    
                    # Ask user to delete item for intended person
                    yOrN=getYOrN("Delete: {} for {} ('y' or 'n')? ".format(recipientInfo[21:50].strip(),nameRmve))
                    
                    # If user enter's 'n' write to temporary file
                    if (yOrN=="n"):
                        print(recipientInfo.strip(),file=fout)
                    
                    # Else add one to delete count
                    else:
                        deleteCount+=1
                
                # Else add one to delete count
                else:
                    deleteCount+=1
            
            # Else write to temporary file
            else:
                print(recipientInfo.strip(),file=fout)
        
        # If delete count is not 0
        # Display total items after writing
        if (deleteCount!=0):    
            print("For {} you deleted {} present".format(nameRmve,deleteCount),end="")
            if (deleteCount>1):
                print("s!")
        
        # Close list file and temporary file
        fin.close()
        fout.close()
        
        # Delete list file
        os.remove(listName)
        
        # Rename temporary file to original file name
        os.rename("temp.txt",listName)
        
        # Call line count function
        lineCount=getLineCount()
        
        # If line count is not 0
        # Display total items after writing
        if (lineCount!=0):
            print("\nAfter deleting for {}: total of {} item".format(nameRmve,lineCount),end="")
            if (lineCount>1):
                print("s!")
    pressEnter()

def searchList(listName):
    """Search for gifts given the list by person
    or store.

    Arguments:
        listName: The name of the list to search.
    """
    
    # Call function to get line count
    lineCount=getLineCount(listName)
    
    # If line count is 0 notify that there are 
    # no items within the list
    if (lineCount==0):
        print("No items within the list.")

    # Else search for item within list
    else:
        
        # Ask user to serach by person or store
        personOrStore=input("Search by 'P'erson or 'S'tore? ").upper()
        
        # If user would like to search by person
        if (personOrStore=="P"):
            
            # Ask for name to search for
            search=input("Enter name to search for: ")
            print("\nPresents to purchase for {}:".format(search))
        
        # Else proceed by store
        else:
            
            # Ask user for store to search for
            search=input("Enter store to search for: ")
            print("\nPresents to purchase at {}:".format(search))
        
        # Open to file to read 
        fin=open(listName,"r")
        searchCount=0
        
        # Start Infinite loop
        while True:
            
            # Read line from file
            line=fin.readline()
            
            # If line is blank exit loop
            if (line==""):
                break
            
            # If name or store is in line
            if (line.strip().find(search)!=-1):
                
                # Add one to search count
                searchCount+=1
                
                # If user searched by person display item and store
                if (personOrStore=="P"):
                    print("{:5}. {} (at {})".format(searchCount,line[21:50].strip(),line[51:70].strip()))
                
                # Else display item and person
                else:
                    print("{:5}. {} (for {})".format(searchCount,line[21:50].strip(),line[:20].strip()))
        
        # Close file
        fin.close()
    pressEnter()

def clearList(fileName):
    """Clear the list for a given file.

    Arguments:
        fileName: The name of the file to clear.
    """

    # Create file
    open(fileName,"w").close()
    pressEnter()

def getNewList():
    """Prompts the user to enter a list name and creates 
    a new file with that name. If no name is provided, 
    the default file name "presents.txt" is used. 
    The name of the new file is added to the list 
    inventory file "listInventory.txt".

    Returns:
        The name of the newly created list file.
    """
    
    # Ask for list name
    fName=input("Enter a list name: ")
    
    # If blank set to "presents.txt"
    if (fName==""):
        
        # Create "presents.txt"
        open("presents.txt","a").close()
        
        # Set file name to "presents.txt"
        fName="presents.txt"
    
    # If list name does not end with ".txt"
    # Add it to the end of entered file name
    if (fName.endswith(".txt")==False):
        fName+=".txt"
    
    # Create file name
    open(fName,"a").close()
    
    # If list exists add it to the directory containing all file names
    if os.path.exists(fName)==False:
        fileList=open("listInventory.txt","a")
        fileList.write(fName+"\n")
    return fName

def chooseList():
    """Prompts the user to select a list from the list 
    inventory file "listInventory.txt" or create a new 
    list. If a new list is chosen, the user is 
    prompted to enter the name of the list and a new 
    file with that name is created.

    Returns:
        The name of the selected list file.
    """
    
    # Open file directory to store all list names
    fileList=open("listInventory.txt","r")
    lineCount=0
    
    # Start infinite loop
    while True:
        
        # Read line from file
        nameList=fileList.readline()
        
        # If line is blank 
        # Exit loop
        if nameList=="":
            break
        lineCount+=1
        
        # Display file names
        print("{}. {}".format(lineCount,nameList.strip()))
    
    # Ask if user would like to enter new list
    newListYOrN=getYOrN("Would you like to create a new list and add it ('y' or 'n')? ")
    
    # If user enters 'y'
    if (newListYOrN=="y"):
        
        # Call function to ask for new file name
        listName=getNewList()
    
    # Start Infinite loop in case user enters value
    while True:
        
        # Ask for list to switch to
        listName=input("Enter name of list to switch to: ")
        
        # If file does not exist
        # Display error message
        if (os.path.exists(listName)==True):
            break
        print("File does not exist, enter a valid file name.")
    return listName

def modifyItem(listName):
    """Prompts the user to enter the name of a person 
    on the list and allows the user to change the gift and store information for that person.
    
    Arguments:
        listName: The name of the list file to be modified.
    """
    
    # Ask user whome they would like to change the gift for
    nameChangeGift=input("Who would you like to change the gift for? ")
    lineTotal=""
    
    # Open file to read
    with open(listName,"r") as fin:
        
        # Start counted loop for lines in file
        for line in fin:
            
            # Add line to total lines
            lineTotal+=line
    
    # Open file to read
    fin=open(listName,"r")
    
    # Start infinte loop
    while True: 
        
        # Read line from file 
        line=fin.readline()
        
        # If blank exit loop
        if (line==""):
            break
        
        # If name to modify gift is in line 
        if (line.strip().find(nameChangeGift)!=-1):
            
            # Ask user if they would like to change item at the store
            chngeYOrN=getYOrN("Would you like to change the {} at {} ('y' or 'n')? ".format(line[21:50].strip(),line[51:70].strip()))
            
            # If user enter's 'y'
            if (chngeYOrN=="y"):
                newGift=input("What is the new gift? ")
                newStore=input("What is the store where the gift can be purchased? ")
                newLine="{:20.20s} {:30.30s} {:20.20s}".format(nameChangeGift,newGift,newStore)
                lineTotal=lineTotal.replace(line.strip(),newLine.strip())
                fin.close()
                fout=open(listName,"w")
                fout.write(lineTotal)
                fout.close()
                print("\nChanges have been made to the list.")
                break

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

def getYOrN(prompt):
    """Ask user to enter 'y' or 'n', given the prompt.
    Error trap to ensure input is either option.

    Arguments:
        prompt: Prompt to ask user.

    Returns:
        Answer either 'y' or 'n' to prompt.
    """
    
    # Start infinite loop
    while True:
        
        # Ask prompt
        yOrN=input(prompt).lower()
        
        # If user does not enter 'y' or 'n' 
        # Display error
        if (yOrN=="y" or yOrN=="n"):
            break
        print("Error, enter either 'y' or 'n'!")
    return yOrN

def getLineCount(listName):
    """Get line count for given list.

    Arguments:
        listName: 
    """
    fin=open(listName,"r")
    lineCount=0
    while True:
        line=fin.readline()
        if (line==""):
            break
        lineCount+=1
    fin.close()
    return lineCount

def pressEnter():
    """Prompt user to press enter.
    """
    input("\nPress [Enter] to continue!\n")

### MAIN PROGRAM ###

import os

# If file to store all the lists does not exist
if (os.path.exists("listInventory.txt")==False):
    
    # Create "listInvetory.txt"
    open("listInventory.txt","w").close()

# Call function to get new list
listName=getNewList()
print("{:*^80s}".format("The Present Manager"))
print("{:^80s}".format("====================="))

# Start infinite loop
while True:
    
    # Display options
    print("\n1 - Create a new list")
    print("2 - Display list")
    print("3 - Add to list")
    print("4 - Delete from list")
    print("5 - Search through list")
    print("6 - Switch list")
    print("7 - Modify Item")
    print("8 - Clear list")
    print("9 - Exit")
    option=validVal(1,9)
    if (option==1):
        createNewList(listName)
    elif(option==2):
        readFromList(listName)
    elif(option==3):
        addToList(listName)
    elif(option==4):
        deleteFromList(listName)
    elif(option==5):
        searchList()
    elif(option==6):
        listName=chooseList()
    elif (option==7):
        modifyItem(listName)
    elif (option==8):
        clearList(listName)
    else:
        print("\nThanks for using The Present Manager!")
        break
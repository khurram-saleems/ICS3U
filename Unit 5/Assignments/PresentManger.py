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
    lineCount=getLineCount(listName)
    if (lineCount>0):
        delete=getYOrN("File contains existing content, delete and write ('y' or 'n')? ")
        if (delete=="n"):
            pressEnter()
            return
    fout=open(listName,"w")
    lineCount=0
    while True:
        name=input("Enter name (blank to exit): ")
        if (name==""):
            break
        present=input("Enter gift to purchase: ")
        store=input("Enter store where product is available: ")
        fout.write("{:20.20s} {:30.30s} {:20.20s}\n".format(name,present,store))
        lineCount+=1
    fout.close()
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
    lineCount=getLineCount(listName)
    if (lineCount==0):
        print("No items within the list.")
    else:
        with open(listName,"r") as fin:
            lineCount=0
            print("\n{:>3s}  {:20} {:30} {:20}".format("Num","Name","Gift","Store"))
            while True:
                recipientInfo=fin.readline()
                if (recipientInfo==""):
                    break
                lineCount+=1
                print("{:3}. {}".format(lineCount,recipientInfo.strip()))
                if (lineCount%20==0):
                    pressEnter()
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
    fout=open(listName,"a")
    while True:
        name=input("Enter name (blank to exit): ")
        if (name==""):
            break
        present=input("Enter gift to purchase: ")
        store=input("Enter store where product is available: ")
        fout.write("{:20.20s} {:30.30s} {:20.20s}\n".format(name,present,store))
    fout.close()
    lineCount=getLineCount(listName)
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
    lineCount=getLineCount(listName)
    if (lineCount==0):
        print("No items within the list.")
    else:
        nameRmve=input("Enter name to delete items for: ")
        allOrSelect=input("'A'll items or 'S'elective? ").upper()
        fin=open(listName,"r")
        fout=open("temp.txt","w")
        deleteCount=0
        while True:
            recipientInfo=fin.readline()
            if (recipientInfo==""):
                break
            if (recipientInfo.strip().find(nameRmve)!=-1):
                if (allOrSelect=="S"):
                    yOrN=getYOrN("Delete: {} for {} ('y' or 'n')? ".format(recipientInfo[21:50].strip(),nameRmve))
                    if (yOrN=="n"):
                        print(recipientInfo.strip(),file=fout)
                    else:
                        deleteCount+=1
                else:
                    deleteCount+=1
            else:
                print(recipientInfo.strip(),file=fout)
        if (deleteCount!=0):    
            print("For {} you deleted {} present".format(nameRmve,deleteCount),end="")
            if (deleteCount>1):
                print("s!")
        fin.close()
        fout.close()
        os.remove("presents.txt")
        os.rename("temp.txt","presents.txt")
        lineCount=getLineCount()
        if (lineCount!=0):
            print("\nAfter deleting for {}: total of {} item".format(nameRmve,lineCount),end="")
            if (lineCount>1):
                print("s!")
    pressEnter()

def searchList(listName):
    lineCount=getLineCount(listName)
    if (lineCount==0):
        print("No items within the list.")
    else:
        personOrStore=input("Search by 'P'erson or 'S'tore? ").upper()
        if (personOrStore=="P"):
            search=input("Enter name to search for: ")
            print("\nPresents to purchase for {}:".format(search))
        else:
            search=input("Enter store to search for: ")
            print("\nPresents to purchase at {}:".format(search))
        fin=open(listName,"r")
        searchCount=0
        while True:
            line=fin.readline()
            if (line==""):
                break
            if (line.strip().find(search)!=-1):
                searchCount+=1
                if (personOrStore=="P"):
                    print("{:5}. {} (at {})".format(searchCount,line[21:50].strip(),line[51:70].strip()))
                else:
                    print("{:5}. {} (for {})".format(searchCount,line[21:50].strip(),line[:20].strip()))
        fin.close()
    pressEnter()

def clearList(fileName):
    open("temp.txt","w").close()
    os.remove(fileName)
    os.rename("temp.txt",fileName)
    pressEnter()

def getNewList():
    fName=input("Enter a list name: ")
    open(fName,"w").close()
    if (fName.endswith(".txt")==False):
        fName+=".txt"
    if os.path.exists(fName)==False:
        fileList=open("listInventory.txt","a")
        fileList.write(fName+"\n")
    if (fName==""):
        open("presents.txt","w").close()
        fName="presents.txt"
    return fName

def chooseList():
    fileList=open("listInventory.txt","r")
    lineCount=0
    while True:
        nameList=fileList.readline()
        if nameList=="":
            break
        lineCount+=1
        print("{}. {}".format(lineCount,nameList.strip()))
    newListYOrN=getYOrN("Would you like to create a new list and add it ('y' or 'n')? ")
    if (newListYOrN=="y"):
        listName=getNewList()
    while True:
        listName=input("Enter name of list to switch to: ")
        if (os.path.exists(listName)==True):
            break
        print("File does not exist, enter a valid file name.")
    return listName

def modifyItem(listName):

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
    while True:
        yOrN=input(prompt).lower()
        if (yOrN=="y" or yOrN=="n"):
            break
        print("Error, enter either 'y' or 'n'!")
    return yOrN

def getLineCount(listName):
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
    input("\nPress [Enter] to continue! ")

### MAIN PROGRAM ###

import os
if (os.path.exists("listInventory.txt")==False):
    open("listInventory.txt","w").close()
listName=getNewList()
print("{:*^80s}".format("The Present Manager"))
print("{:^80s}".format("====================="))
while True:
    print("\n1 - Create a new list")
    print("2 - Display list")
    print("3 - Add to list")
    print("4 - Delete from list")
    print("5 - Search through list")
    print("6 - Switch list")
    print("7 - Modify Item")
    print("7 - Clear list")
    print("8 - Exit")
    option=validVal(1,7)
    if (option==1):
        createNewList(listName)
    elif(option==2):
        readFromList(listName)
    elif(option==3):
        addToList()
    elif(option==4):
        deleteFromList(listName)
    elif(option==5):
        searchList()
    elif(option==6):
        listName=chooseList()
    elif (option==7):
        clearList(listName)
    else:
        print("\nThanks for using The Present Manager!")
        break
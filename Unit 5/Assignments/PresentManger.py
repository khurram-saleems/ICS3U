#     Assignment | Assignment 5-2
#  Program Title | The Present Manager
#                |
#     Written by | Khurram Shaikh
#           Date | Thursday, December 22, 2022
#                |
#    Description | This program 

def createNewList():
    lineCount=getLineCount()
    if (lineCount>0):
        delete=getYOrN("File contains existing content, delete and write ('y' or 'n')? ")
        if (delete=="n"):
            pressEnter()
            return
    fout=open("presents.txt","w")
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

def readFromList():
    lineCount=getLineCount()
    if (lineCount==0):
        print("No items within the list.")
    else:
        with open("presents.txt","r") as fin:
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

def addToList():
    fout=open("presents.txt","a")
    while True:
        name=input("Enter name (blank to exit): ")
        if (name==""):
            break
        present=input("Enter gift to purchase: ")
        store=input("Enter store where product is available: ")
        fout.write("{:20.20s} {:30.30s} {:20.20s}\n".format(name,present,store))
    fout.close()
    lineCount=getLineCount()
    if (lineCount!=0):
        print("After adding to list: total of {} item".format(lineCount),end="")
        if (lineCount>1):
            print("s!")
    pressEnter()

def deleteFromList():
    lineCount=getLineCount()
    if (lineCount==0):
        print("No items within the list.")
    else:
        nameRmve=input("Enter name to delete items for: ")
        allOrSelect=input("'A'll items or 'S'elective? ").upper()
        fin=open("presents.txt","r")
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

def searchList():
    lineCount=getLineCount()
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
        fin=open("presents.txt","r")
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

def clearList():
    open("temp.txt","w").close()
    os.remove("presents.txt")
    os.rename("temp.txt","presents.txt")
    pressEnter()

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

def getLineCount():
    fin=open("presents.txt","r")
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
print("{:*^80s}".format("The Present Manager"))
print("{:^80s}".format("====================="))
while True:
    print("\n1 - Create a new list")
    print("2 - Display list")
    print("3 - Add to list")
    print("4 - Delete from list")
    print("5 - Search through list")
    print("6 - Clear list")
    print("7 - Exit")
    option=validVal(1,7)
    if (option==1):
        createNewList()
    elif(option==2):
        readFromList()
    elif(option==3):
        addToList()
    elif(option==4):
        deleteFromList()
    elif(option==5):
        searchList()
    elif(option==6):
        clearList()
    else:
        print("\nThanks for using The Present Manager!")
        break
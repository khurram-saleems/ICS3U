#     Assignment | Assignment 5-2
#  Program Title | Present Manager
#                |
#     Written by | Khurram Shaikh
#           Date | Thursday, December 22, 2022
#                |
#    Description | This program 

def createNewList():
    list=open("presents.txt","w")
    while True:
        name=input("Enter name (blank to exit): ")
        if (name==''):
            break
        present=input("Enter gift to purchase: ")
        store=input("Enter store where product is available: ")
        print(name,"\n"+present,"\n"+store,file=list)
    list.close()

def readFromList():
    with open("presents.txt","r") as list:
        itemCount,lineCount=0,0
        print("\n{:>3s}  {:20} {:30} {:20}".format("Num","Name","Gift","Store"))
        while True:
            name=list.readline()
            if name=="":
                break
            lineCount+=1
            name=name.strip()
            present=list.readline().strip()
            if (present!=""):
                itemCount+=1
            store=list.readline().strip()
            print("{:3}. {:20.20s} {:30.30s} {:20.20s}".format(lineCount,name,present,store))
            if (lineCount%20==0):
                input("Press [Enter] to return to the menu: ")
    print("Total of {} present".format(itemCount),end="")
    if (itemCount>1):
        print("s!")

def addToList():
    list=open("presents.txt","a")
    while True:
        name=input("Enter name (blank to exit): ")
        if (name==''):
            break
        present=input("Enter gift to purchase: ")
        store=input("Enter store where product is available: ")
        print(name,"\n"+present,"\n"+store,file=list)

def getYOrN(prompt):
    while True:
        yOrN=input(prompt)
        if (yOrN=="y" or yOrN=="n"):
            break
        print("Error, enter either 'y' or 'n'!")

def deleteFromList():
    name=input("Enter name to delete items for: ")
    allOrSelective=input("Would you like to remove 'A'll items or 'S'elective? ").upper()
    oldList=open("presents.txt","r")
    newList=open("temp.txt","w")
    while True:
        namePresentStore=oldList.readline()
        if namePresentStore=="":
            break 
        if (namePresentStore.strip()==name):    
            present=oldList.readline().strip()
            store=oldList.readline()
            if (allOrSelective=="S"):
                deleteItem=getYOrN("Would you like to delete {} for {} ('y' or 'n')? ".format(present,name.strip()))
        if (namePresentStore.strip()!=name):
            if (deleteItem=='y'):
                print(namePresentStore.strip(),file=newList)
            if (allOrSelective=="A"):
                print(namePresentStore.strip(),file=newList)
    oldList.close()
    newList.close()
    os.remove("presents.txt")
    os.rename("temp.txt","presents.txt")

import os
createNewList()
readFromList()
deleteFromList()
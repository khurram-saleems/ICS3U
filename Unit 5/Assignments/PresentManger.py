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
        if name=="":
            break
        present=input("Enter gift to purchase: ")
        store=input("Enter store where product is available: ")
        list.write("{:20.20s} {:30.30s} {:20.20s}\n".format(name,present,store))
    list.close()

def readFromList():
    with open("presents.txt","r") as list:
        lineCount=0
        print("\n{:>3s}  {:20} {:30} {:20}".format("Num","Name","Gift","Store"))
        while True:
            recipientInfo=list.readline()
            if recipientInfo=="":
                break
            lineCount+=1
            print("{:3}. {}".format(lineCount,recipientInfo.strip()))
            if (lineCount%20==0):
                input("Press [Enter] to return to the menu: ")
    print("Total of {} present".format(lineCount),end="")
    if (lineCount>1):
        print("s!")

def addToList():
    list=open("presents.txt","a")
    while True:
        name=input("Enter name (blank to exit): ")
        if name=="":
            break
        present=input("Enter gift to purchase: ")
        store=input("Enter store where product is available: ")
        list.write("{:20.20s} {:30.30s} {:20.20s}\n".format(name,present,store))
    list.close()

def getYOrN(prompt):
    while True:
        yOrN=input(prompt)
        if (yOrN=="y" or yOrN=="n"):
            break
        print("Error, enter either 'y' or 'n'!")

def deleteFromList():
    nameRmve=input("Enter name to delete items for: ")
    userChoice=input("Would you like to remove 'A'll items or 'S'elective? ").upper()
    oldList=open("presents.txt","r")
    newList=open("temp.txt","w")
    if (userChoice=="A"):
        while True:
            line=oldList.readline()
            if line=="":
                break
            if line.find(nameRmve)==-1:
                newList.write(line)
    if (userChoice=="S"):
        while True:
            line=oldList.readline()
            if line=="":
                break
            if line.find(nameRmve)==-1:
                yOrN=getYOrN("Delete {} ('y' or 'n')? ".format(line))

import os
createNewList()
readFromList()
deleteFromList()
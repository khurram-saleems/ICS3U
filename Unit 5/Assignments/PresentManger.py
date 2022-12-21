#     Assignment | Assignment 5-2
#  Program Title | Present Manager
#                |
#     Written by | Khurram Shaikh
#           Date | Thursday, December 22, 2022
#                |
#    Description | This program 

def createNewList():
    fout=open("presents.txt","w")
    while True:
        name=input("Enter name (blank to exit): ")
        if name=="":
            break
        present=input("Enter gift to purchase: ")
        store=input("Enter store where product is available: ")
        fout.write("{:20.20s} {:30.30s} {:20.20s}\n".format(name,present,store))
    fout.close()

def readFromList():
    with open("presents.txt","r") as fin:
        lineCount=0
        print("\n{:>3s}  {:20} {:30} {:20}".format("Num","Name","Gift","Store"))
        while True:
            recipientInfo=fin.readline()
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
    fout=open("presents.txt","a")
    while True:
        name=input("Enter name (blank to exit): ")
        if name=="":
            break
        present=input("Enter gift to purchase: ")
        store=input("Enter store where product is available: ")
        fout.write("{:20.20s} {:30.30s} {:20.20s}\n".format(name,present,store))
    fout.close()

def getYOrN(prompt):
    while True:
        yOrN=input(prompt)
        if (yOrN=="y" or yOrN=="n"):
            break
        print("Error, enter either 'y' or 'n'!")
    return yOrN

def deleteFromList():
    nameRmve=input("Enter name to delete items for: ")
    allOrSelect=input("'A'll items or 'S'elective? ").upper()
    fin=open("presents.txt","r")
    fout=open("temp.txt","w")
    deleteCount=0
    while True:
        recipientInfo=fin.readline()
        if recipientInfo=="":
            break
        if recipientInfo.strip().find(nameRmve)!=-1:
            if allOrSelect=="S":
                yOrN=getYOrN("Delete {} ('y' or 'n')? ".format(recipientInfo))
                if yOrN=="n":
                    print(recipientInfo.strip(),file=fout)
                deleteCount+=1
        else:
            print(recipientInfo.strip(),file=fout)
    print("You deleted {} presents for {}.\n".format(deleteCount,nameRmve))
    fin.close()
    fout.close()
    os.remove("presents.txt")
    os.rename("temp.txt","presents.txt")

def searchList():
    personOrStore=input("Search by 'P'erson or 'S'tore? ").upper()
    if personOrStore=="P":
        search=input("Enter name to search for: ")
        print("Presents to purchase at {}:".format(search))
    else:
        search=input("Enter store to search for: ")
        print("Presents to purchase at {}:".format(search))
    fin=("presents.txt","r")
    searchCount=0
    while True:
        line=fin.readline()
        if line=="":
            break
        searchInfo=line.strip().split()
        if searchInfo.find(search)!=-1:
            searchCount+=1
            if personOrStore=="P":
                print("{}. {} (at {})".format(searchCount,searchInfo[2],searchInfo[3]))
            else:
                print("{}. {} (for {})".format(searchCount,searchInfo[2],searchInfo[1]))
    fin.close()



    
import os
addToList()
readFromList()
searchList()
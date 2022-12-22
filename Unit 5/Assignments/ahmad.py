import os
import os.path
def displayFile(file):
    fout=open(file, "r")
    while True:
        line=fout.readline()
        if line=="":
            break
        print(line.strip())
    fout.close()
def validVal(num1,num2):
    while True:
        num=int(input())
        if num>=num1 and num<=num2:
            break
        print("Invalid Input")
    return num
def validOpt(sen,letter1,letter2):
    while True:
        opt=input(sen)
        if opt==letter1 or opt==letter2:
            break
        print("Invalid Input")
    return opt
def fileOption(file,fileOpt):
    file=open(file,fileOpt)
    while True:
        name=input("Enter Name([s] to stop): ")
        if name == "s":
            break
        gift=input("Enter Gift: ")
        store=input("Enter Store: ")
        line="{:<15.10s}{:<20.15s}{:<20.15s}".format(name,gift,store)+"\n"
        file.write(line)
def fileExists():
    while True:
        file=input("Enter File Name: ")
        file=endsWith(file)
        fileExists=os.path.exists(file)
        if fileExists==False:
            return file
        replace=input("File Already Exists ([r]eplace file): ")
        if replace=="r":
            break
    return file
def endsWith(fileName):
    if fileName.endswith(".txt")==False:
        fileName+=".txt"
    return fileName
def deleteFile(file):
    found=False
    displayFile(file)
    deleteOpt=validOpt("Would you like to delete [n]ame or [s]tore?: ","n","s")
    fout=open(file,"r")
    save=open("tempFile.txt","w")
    if deleteOpt=="n":
        word2=input("Enter Name: ")
        item="Name"
        num1=0
        num2=15
    elif deleteOpt=="s":
        word2=input("Enter Store: ")
        item="Store"
        num1=35
        num2=55
    while True:
        line=fout.readline()
        word=line[num1:num2].strip()
        if line=="":
            break
        if word!=word2:
            save.write(line)
        elif word==word2:
            found=True
    if found==True:
        print()
        print("{} was deleted from the list.".format(word2))
    else:
        print()
        print("{} was not found nothing was delete.".format(item))
    save.close()
    fout.close()
    os.remove(file)
    os.rename("tempFile.txt",file)
def searchFile(file):
    itemList=""
    lineCount=0
    lineReset=0
    deleteOpt=validOpt("Would you like to search using [n]ame or [s]tore?: ","n","s")
    read=open(file,"r")
    if deleteOpt=="n":
        name=input("Enter Name: ")
        num1=0
        num2=15
    elif deleteOpt=="s":
        name=input("Enter Store: ")
        num1=35
        num2=55
    while True:
        line=read.readline()
        if line=="":
            break
        if lineReset==20:
            lineReset=0
            input("Enter to Continue")
        if line[num1:num2].strip()==name:
            lineReset+=1
            lineCount+=1
            print()
            itemList+=("({:3d}). {}".format(lineCount,line[15:35].strip())+"\n")
    print()
    
    if itemList!="":
        print("You need to buy")
        print(itemList)
    else:
        print("No item were found.")
def checkingFiles(file):
        readList=open(file,"r")
        newList=open("tempFile.txt","w")
        lineCount=0
        while True:
            lineRead=readList.readline()
            if lineRead=="" and lineCount==0:
                emptyList=True
            if lineRead=="":
                break
            fileExists=os.path.exists(lineRead.strip()+".txt")
            if fileExists==True:
                newList.write(lineRead.strip()+"\n")
        readList.close()
        newList.close()
        os.remove(file)
        os.rename("tempFile.txt",file)
while True:
    checkingFiles("Presents List.txt")
    checkingFiles("Current File.txt")
    readFile=open("Current File.txt","r")
    line=readFile.readline()
    if line=="":
        DiselcList="No List Selected"
    else:
        DiselcList=line.strip()
        selcList=line.strip()+".txt"
    readFile.close()
    print("Selected List: {}".format(DiselcList))
    print("1. Change List")
    print("2. Create New List")
    print("3. View List")
    print("4. Add to List")
    print("5. Delete From List")
    print("6. Search List")
    print("7. Clear List")
    print("8. Delete List")
    print("9. Exit")
    option=validVal(1,9)
    if option==1:
        readFile2=open("Presents List.txt","r")
        line2=readFile2.readlines()
        if len(line2)==0:
            print()
            print("There are no lists, you should create some!")
            readFile2.close()
        else:
            lineCount=0
            readFile2=open("Presents List.txt","r")
            while True:
                line2=readFile2.readline()
                if line2=="":
                    break
                lineCount+=1
                print("({:3d}): {}".format(lineCount,line2.strip()))
            num=validVal(1,lineCount)
            readFile2=open("Presents List.txt","r")
            line2=readFile2.readlines()[num-1]
            readFile2.close()
            saveFile=open("Current File.txt","w")
            saveFile.write(line2)
            saveFile.close()
    elif option==2:
        fileName=fileExists()
        fileOption(fileName,"w")
        fileName=(fileName.replace(".txt","")+"\n")
        add=open("Presents List.txt","a")
        add.write(fileName)
        add.close()
    elif option==9:
        break
    if DiselcList!="No List Selected":
        if option==3:
            displayFile(selcList)
        elif option==4:
            displayFile(selcList)
            print()
            fileOption(selcList,"a")
        elif option==5:
            deleteFile(selcList)
        elif option==6:
            searchFile(selcList)
        elif option==7:
            clear=validOpt(("Are you sure you want to clear {}(y or n)?: ".format(selcList)),"y","n")
            if clear=="y":
                clearFile=open(selcList,"w")
                clearFile.close()
                print()
                print("List Cleared")
        elif option==8:
            deleteList=validOpt(("Are you sure you want to delete {}(y or n)?: ".format(selcList)),"y","n")
            if deleteList=="y":
                os.remove(selcList)
                print()
                print("List Deleted")
    else:
        print()
        print("No List selected!")
    print()
    input("Press Enter")
    print("\n"*15)
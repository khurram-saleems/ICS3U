def fileName():
    fileName=input("Enter file name: ")
    if (fileName.endswith(".txt")==False):
        fileName+=".txt"
    return fileName

def writeFile():
    writeFile= fileName()
    fout= open(writeFile,"w")
    while True:
        friend= input("Enter the name of a friend ('STOP' to exit): ")
        if friend=="STOP":
            break
        fout.write("{}\n".format(friend))
    fout.close()

def readFile():
    readFile=fileName()
    fin=open(readFile,"r")
    friendCount=0
    while True:
        line= fin.readline()
        if line=="":
            break
        friendCount+=1
        print(line.strip())
    fin.close()
    return friendCount

###MAIN###

while True:
    print("\nOption 1: Write to a file")
    print("Option 2: Read from a file")
    print("Option 3: Exit program\n")
    while True:
        userOption= int(input("Enter option: "))
        if 1<=userOption<=3:
            break
        print("Error, enter an option between 1 and 3.")
    if userOption==1:
        readFile()
    elif userOption==2:
        friends= writeFile()
        print("Total count of friends: {}.".format(friends))
    else:
        break
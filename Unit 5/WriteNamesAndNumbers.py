def getFileName():
    fName=input("Enter file name: ")
    if (fName==""):
        fName="friends.txt"
    if (fName.endswith(".txt")==False):
        fName+=".txt"
    return fName
fileName=getFileName()
fout=open(fileName,"w")
while True:
    print("Enter a friend's name:")
    name=input("-> ")
    if (name=="STOP"):
        break
    phone=input("Phone Number: ")
    fout.write(name+"\n")
    fout.write(phone+"\n")
fout.close()


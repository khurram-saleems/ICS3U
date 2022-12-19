def getFileName():
    fName=input("Enter file name: ")
    if (fName==""):
        fName="friends.txt"
    if (fName.endswith(".txt")==False):
        fName+=".txt"
    return fName
import os
fileName=getFileName()
nameRemove=input("Enter name to remove: ")
fin=open(fileName,"r")
fout=open("temp.txt","w")
while True:
    namePhone=fin.readline()
    if namePhone=="":
        break
    elif namePhone.strip()==nameRemove:
        phone=fin.readline()
    #elif namePhone.strip()!=nameRemove:
    else:
        print(namePhone.strip(),file=fout)
fin.close()
fout.close()
os.remove(fileName)
os.rename("temp.txt",fileName)
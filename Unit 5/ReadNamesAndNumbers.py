def getFileName():
    fName=input("Enter file name: ")
    if (fName==""):
        fName="friends.txt"
    if (fName.endswith(".txt")==False):
        fName+=".txt"
    return fName
fileName=getFileName()
fin=open(fileName,"r")
while True:
    name=fin.readline()
    if name=="":
        break
    name=name.strip()
    phone=fin.readline().strip()
    print("{:30} {:>20}".format(name,phone))
fin.close()

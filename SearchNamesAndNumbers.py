def getFileName():
    fName=input("Enter file name: ")
    if (fName==""):
        fName="friends.txt"
    if (fName.endswith(".txt")==False):
        fName+=".txt"
    return fName
fileName=getFileName()
searchName=input("Enter name to search for: ")
fin=open(fileName,"r")
while True:
    name=fin.readline()
    if name=="":
        break
    name=name.strip()
    phone=fin.readline().strip()
    if name in searchName:    
        print("{:30} {:>20}".format(name,phone))


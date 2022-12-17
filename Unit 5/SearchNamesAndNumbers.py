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
    phone=fin.readline().strip()
    if name.find(searchName)!=-1:    
        print("{:30} {:>20}".format(name.strip(),phone))


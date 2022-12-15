fileName=input("Enter file name: ")
if (fileName==""):
    fileName="friends.txt"
if (fileName.endswith(".txt")==False):
    fileName+=".txt"
fout=open(fileName,"a")
while True:
    print("Enter a friend's name:")
    name=input("-> ")
    if (name=="STOP"):
        break
    phone=input("Phone Number: ")
    fout.write(name+"\n")
    fout.write(phone+"\n")
fout.close()

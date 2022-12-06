fileIn=open("reindeer.txt","r")
print("Santas reindeer are called:")
while True:
    name=fileIn.readline()
    if name=="":
        break
    print(name)
fileIn.close()
print("some random text")
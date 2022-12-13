#     Assignment | Assignment 5-1
#  Program Title | Command Finder
#                |
#     Written by | Khurram Shaikh
#           Date | Friday, December 9, 2022
#                |
#    Description | This program 

def findCommand(fileName,command):
    lineCount=0
    fin=open(fileName,"r")
    while True: 
        line=fin.readline()
        if line=="":
            break
        lineCount+=1
        if line.strip().find(command)!=-1:
            print("({})      {}".format(lineCount,line.strip()))



# Start infinite loop
while True: 
    
    # Ask user to enter filename
    fileName=input("Enter a Python filename: ")
    
    # If filename does not end with '.py' extension add it
    if (fileName.endswith(".py")==False):
        fileName+=".py"
    
    # Ask user for command
    command=input("Enter the command you are searching for: ")
    findCommand(fileName,command)



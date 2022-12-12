# Open the file 
fin=open("greetings.txt","r") 

# Start a loop since we don't know how many lines are in the file 
while True: 

    # read a line from the file 
    line = fin.readline() 

    # if string is blank exit loop 

    if line=="": 

        break 
    print(line, end="") 

# Close the file 
fin.close() 


while True:
    youngerSibling=int(input("Enter younger siblings: "))
    if (youngerSibling>=0):
        break
    print("Error! Enter a whole number greater than 0.")
while True:
    olderSiblings=int(input("Enter older siblings: "))
    if (olderSiblings>=0):
        break
    print("Error! Enter a whole number greater than 0.")

if (olderSiblings>0 and youngerSibling>0):
    print("You are the middle child.")

elif (olderSiblings>0 and youngerSibling==0):
    print("You are the youngest child.")

elif (olderSiblings==0 and youngerSibling==0):
    print("You are the only child.")
def getYorN(q):
    print(q)
    while True:
        yOrN=input("Enter 'y' or 'n'.").lower()
        if (yOrN=='y' or yOrN=='n'):
            break
        print("Error! Enter 'y' or 'n'.")
    return yOrN
question=input("Enter question: ")
answer=getYorN(question)
def validVal(x,y):
    while True:
        v=int(input("Enter a value: "))
        if (v>=x and v<=y):
            break
        print('error')
    return v
choice=validVal(1,5)
print(choice)


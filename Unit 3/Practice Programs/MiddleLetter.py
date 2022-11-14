while True:
    w=input("Enter a word: ")
    if (w==""):
        break
    elif (len(w)%2==0):
        print("Word entered has an even number of characters.")
    else:
        print("Middle letter is: {}".format(w[len(w)//2]))

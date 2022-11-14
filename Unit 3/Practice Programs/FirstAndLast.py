while True:
    w=input("Enter a word: ")
    if (len(w)>1):
        break
    print("Error enter a word greater than 1.")
print('{}{}'.format(w[0],w[-1]))
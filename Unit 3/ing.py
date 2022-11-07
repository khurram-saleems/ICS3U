while True:
    text=input("\nEnter a string: ")
    if (text.find("ing")):
        print("Ding! Ding! Found an ing!, {} ing".format(text.count("ing")),end="")
        if (text.count("ing")>1):
            print("s")
    else:
        print("Display no ing found")
        break
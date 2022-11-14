while True:
    symbol=input("Character you would like to repeat: ")
    amount=int(input("How many {} do you want? ".format(symbol)))
    print(symbol*amount)
    
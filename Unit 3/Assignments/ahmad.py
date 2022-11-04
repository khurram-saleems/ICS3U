while True: 

    while True: 

        sent=input("Enter Sentence: ") 

        length=len(sent) 

        firstL=sent[0:1] 

        capital=firstL.isupper() 

        if length >=5 and capital==True: 

            break 

        print("Sentence has to be longer than 5 letters, and have proper punctuation.") 

    for i in reversed(range(0,length+1)): 

        word=sent[0:i] 

        length=length-1 

        print(word) 

    length=len(sent) 

    for i in range(0,length+1): 

        word=sent[i:length] 

        print(" "*i+word) 

    loop=input("Do you want to loop? (y or n): ") 

    if loop=="n": 

        break
# 01 Practice Programs 1 
# Program 3: Multiple Choice Quiz Questions
#
# Khurram Shaikh
# Monday, October 3, 2022
#
# This program asks user to respond to a multiple choice question,
# displays a personalized sentence for each selection

question = (input("What is 5^2? Enter 'A','B','C','D','E'\n(A) 50\n(B) 42\n(C) 125\n(D) 75\n(E) 25\n"))
if (question=="A"):
    print("50% of this is the correct answer, try again next time.")
elif(question=="B"):
    print("42 is not the correct answer, it is a multiple of the factors 6 and 7.")
elif(question=="C"):
    print("This is 5^3, not 5^2.")
elif(question=="D"):
    print("That is three time's the actual answer.")
elif(question=="E"):
    print("Nice, 25 is the correct answer!")

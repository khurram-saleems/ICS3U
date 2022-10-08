# 06 Practice Programs 1 
# Program 3: Multiple Choice Quiz Questions
#
# Khurram Shaikh
# Friday, October 7, 2022
#
# This program asks user to respond to a multiple choice question,
# displays a personalized sentence for each selection

# Start infinite loop incase user enters invalid value
while True:
    
    # Ask user what 5^2 is
    answer = (input("What is 5^2? Enter 'A','B','C','D','E'\n(A) 50\n(B) 42\n(C) 125\n(D) 75\n(E) 25\n"))
    
    # If answer is not between 'A' and 'E' 
    # Display error message
    if (answer>="A" and answer<="E"):
        break
    print("Error! Please enter a value between 'A' and 'E'.")
if (answer=="A"):
    print("50% of this is the correct answer, try again next time.")
elif(answer=="B"):
    print("42 is not the correct answer, it is a multiple of the factors 6 and 7.")
elif(answer=="C"):
    print("This is 5^3, not 5^2.")
elif(answer=="D"):
    print("That is three time's the actual answer.")
elif(answer=="E"):
    print("Nice, 25 is the correct answer!")

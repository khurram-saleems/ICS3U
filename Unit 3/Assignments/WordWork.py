#     Assignment | Assignment 3-2
#  Program Title | The Word Food Processor 
#                |
#     Written by | Khurram Shaikh
#           Date | Tuesday, November 8, 2022
#                |
#    Description | 

# Ask user for string
sentence=input("Enter a sentence:")
# Display prompt for option
print("Choose an option:")
print("1 - display a sentence in reverse order")

# Ask for option
option=int(input())

# If option is 1 display reverse order of string
if (option==1):
    for i in reversed(range(len(sentence))):
        print(sentence[i],end="")
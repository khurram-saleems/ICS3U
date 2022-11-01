# 02 Practice Programs 1 
# Program 1: Average Word Length
#
# Khurram Shaikh
# Monday, October 31, 2022
#
# This program asks for the user to enter ten 
# random words, and then displays the 
# character average.

t=0 
for x in range (1,11): 
    w=input("Enter word: ") 
    t+=len(w) 
print("Average is {}".format(t/x)) 
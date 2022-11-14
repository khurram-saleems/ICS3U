# 02 Practice Programs 1b
# Program 1: Average Word Length Extended
#
# Khurram Shaikh
# Monday, October 31, 2022
#
# This program asks for the user to enter ten 
# random words, and then displays the 
# character average.

t,x=0,0 
while True: 
    w=input("Enter word: ")
    if (w==""):
        break
    x+=1 
    t+=len(w)
     
print("Average is {}, total is {}".format(t/x,t)) 
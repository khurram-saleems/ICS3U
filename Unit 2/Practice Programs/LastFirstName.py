# 10 Practice Programs 2
# Program 5: Last First Name 
#
# Khurram Shaikh
# Friday, October 14, 2022
#
# This program asks the user to enter 10 names, outputs 
# the name that is alphebetically last.

low=""
for x in range(10):
    name=input("Enter your first name: ")
    if (name>low):    
        low=name
print("The name that is alphebetically last is {}".format(low))
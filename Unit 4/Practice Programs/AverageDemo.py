# 01 Practice Programs 4
# Program 1: First and last letter
#
# Khurram Shaikh
# Sunday, November 27, 2022
#
# This program asks the user for numbers and
# displays the average.

def calcAvg(n1,n2,n3,n4):
    return (n1+n2+n3+n4)/4
v1=int(input("Num 1:"))
v2=int(input("Num 2:"))
v3=int(input("Num 3:"))
v4=int(input("Num 4:"))
avg=calcAvg(v1,v2,v3,v4)
print("Average is: {}".format(avg))
# 01 Practice Programs 3
# Program 1: Cuber
#
# Khurram Shaikh
# Sunday, November 27, 2022
#
# This program cubes and displays an entered value.

def cubeNum(v):
    print(v**3)
while True:
    n=int(input("Enter a number to cube ('0' to exit): "))
    if (n==0):
        break
    cubeNum(n)
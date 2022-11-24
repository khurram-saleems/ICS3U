#     Assignment | Assignment 3-1
#  Program Title | Math Helper
#                |
#     Written by | Khurram Shaikh
#           Date | Thursday, October 24, 2022
#                |
#    Description | This program

def areaOfTriangle(b,h):
    a=b*h/2
    return a
def pythagorasTheorem(a,b,c):
    c=math.sqrt(a^2+b^2)
    return c
def quadraticFormula(a,b,c):
    s1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    s2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    return s1,s2
import math
print("1 - Area of a triangle")
print("2 - Pythagoras' theorem")
print("3 - Quadratic formula")
option=int(input("Choose a formula: "))
if (option==1):
    print("{:^80s}".format('Area of a triangle'))
    base=int(input("Enter base value: "))
    height=int(input("Enter height value: "))
    area=areaOfTriangle(base,height)
    print(area)
elif (option==2):
    sideA=float(input("Enter side A value: "))
    sideB=float(input("Enter side B value: "))
    sideC=pythagorasTheorem(sideA,sideB)
    print(sideC)
elif(option==3):
    aVal=float(input("Enter A value: "))
    bVal=float(input("Enter B value: "))
    cVal=float(input("Enter C value: "))
    zeros=quadraticFormula(aVal,bVal,cVal)
    print(zeros)

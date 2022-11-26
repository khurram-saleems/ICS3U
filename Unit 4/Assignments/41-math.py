#     Assignment | Assignment 3-1
#  Program Title | Math Helper
#                |
#     Written by | Khurram Shaikh
#           Date | Thursday, October 24, 2022
#                |
#    Description | This program 

def showTitle():
    if (option==1):
        print("{:^80s}".format("Area of triangle"))
    elif (option==2):
        print("{:^80s}".format("Pythagoras' theorem"))
    elif (option==3):
        print("{:^80s}".format("Quadratic formula"))
    elif (option==4):
        print("{:^80s}".format("Area of trapezoid"))
    elif (option==5):
        print("{:^80s}".format("Circumference"))
    elif (option==6):
        print("{:^80s}".format("Area of circle"))
    elif (option==7):
        print("{:^80s}".format("Factorials"))
    else: 
        print("{:^80s}".format("Surface area of a cone"))
def units():
    u=input("Enter abbreviated unit of length: ")
    return u
def areaOfTriangle(b,h):
    a=b*h/2
    return a
def pythagorasTheorem(a,b,c):
    c=math.sqrt(a^2+b^2)
    return c
def quadraticFormula(a,b,c):
    d=(b**2)-(4*a*c)
    if (d>0):   
        print("({},0) and ({},0) are the zeros.".format((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a)))
    elif (d==0):
        print(-b/(2*a))
    else:
        print("No zeros in quadratic relation.")
def areaOfTrapezoid(a,b,h):
    A=((a+b)/2)*h
    return A
def circumference(r):
    c=2*math.pi*r
    return c
def areaCircle(r):
    A=math.pi(r**2)
    return A
import math
print("{:*^80s}".format("Math Helper"))
while True:
    print("1 - Area of a triangle")
    print("2 - Pythagoras' theorem")
    print("3 - Quadratic formula")
    print("4 - Area of trapezoid")
    print("5 - Circumference")
    print("6 - Area of circle")
    print("7 - Factorials")
    print("8 -  Quit/Exit")
    while True:
        option=int(input("Choose a formula: "))
        if (option>=1 and option<=5):
            break
        print("Error, select an option between 1 and 9.")
    if (option==1):
        showTitle()
        unit=units()
        base=float(input("Enter base: "))
        height=float(input("Enter height: "))
        areaTriangle=areaOfTriangle(base,height)
        print("Area of the triangle is: {} {}².".format(areaTriangle,unit))
    elif (option==2):
        showTitle()
        unit=units()
        sideA=float(input("Enter side A value: "))
        sideB=float(input("Enter side B value: "))
        sideC=pythagorasTheorem(sideA,sideB)
        print("Length of side C is: {} {}.".format(sideC,unit))
    elif (option==3):
        showTitle()
        aVal=float(input("Enter A value: "))
        bVal=float(input("Enter B value: "))
        cVal=float(input("Enter C value: "))
        quadraticFormula(aVal,bVal,cVal)
    elif (option==4):
        showTitle()
        unit=units()
        aBase=float(input("Enter base A: "))
        bBase=float(input("Enter base B: "))
        height=float(input("Enter height: "))
        areaTrapezoid=areaOfTrapezoid(aBase,bBase,height)
        print("Area of triangle is: {} {}.²".format(areaTrapezoid,unit))
    elif (option==5):
        showTitle()
        unit=units()
        radius=input("Enter radius: ")
        circleLength=circumference(radius)
        print("Length of circle is: {} {}.²".format(circleLength,unit))
    elif (option==6):
        showTitle()
        
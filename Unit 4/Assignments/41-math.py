#     Assignment | Assignment 3-1
#  Program Title | Math Helper
#                |
#     Written by | Khurram Shaikh
#           Date | Thursday, October 24, 2022
#                |
#    Description | This program 

def showTitle():
    """Displays title of user's selected formula.
    """
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
    else:
        print("{:^80s}".format("Factorials"))
def units():
    """Asks and returns preferred unit of length.

    Returns:
    User's preferred unit of length.
    """
    u=input("Enter abbreviated unit of length: ")
    return u
def areaOfTriangle(b,h):
    """Calculate and return area of triangle,
    given user's base and height value.

    Arguments:
        b: base of triangle
        h: height of triangle
    
    Returns:
        Area of triangle.
    """
    a=b*h/2
    return a
def pythagorasTheorem(a,b,c):
    c=math.sqrt(a^2+b^2)
    return c
def quadraticFormula(a,b,c):
    d=(b**2)-(4*a*c)
    if (d>0):   
        print("({:.2f},0) and ({:.2f},0) are the zeros.".format((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a)))
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
def factorial(n):
    n=math.factorial(n)
    return n
import math
print("{:*^80s}".format("Math Helper"))

# Start infinite loop 
while True:
    
    # Display available math formulas/functions
    print("1 - Area of a triangle")
    print("2 - Pythagoras' theorem")
    print("3 - Quadratic formula")
    print("4 - Area of trapezoid")
    print("5 - Circumference")
    print("6 - Area of circle")
    print("7 - Factorials")
    print("8 -  Quit/Exit")
    
    # Call function asking for preferred unit
    unit=units()
    
    # Start infinite loop in case user enters invalid value
    while True:
        
        # Ask user to select a formula
        option=int(input("Choose a formula: "))
        
        # If option is not between 1 and 5
        # Display error message
        if (option>=1 and option<=5):
            break
        print("Error, select an option between 1 and 9.")
    
    # If option is 1
    if (option==1):
        
        # Display title of formula/math function
        showTitle()
        
        # Ask user to enter base 
        base=float(input("Enter base: "))
        
        # Ask user for height 
        height=float(input("Enter height: "))
        
        # Call function to calculate and save area of triangle
        areaTriangle=areaOfTriangle(base,height)
        
        # Display area of triangle
        print("Area of the triangle is: {} {}².".format(areaTriangle,unit))
    
    # Else if option is 2
    elif (option==2):
        
        # Display title of formula/math function
        showTitle()
        
        # Ask user for side A
        sideA=float(input("Enter side A value: "))
        
        # Ask user for side B
        sideB=float(input("Enter side B value: "))
        
        # Call function to calculate length of hypotenuse
        sideC=pythagorasTheorem(sideA,sideB)
        
        # Display length of side C
        print("Length of side C is: {} {}.".format(sideC,unit))
    
    # Else if option is 3
    elif (option==3):

        # Display title of formula/math function
        showTitle()

        # A
        aVal=float(input("Enter A value: "))
        bVal=float(input("Enter B value: "))
        cVal=float(input("Enter C value: "))
        quadraticFormula(aVal,bVal,cVal)
    elif (option==4):
        showTitle()
        aBase=float(input("Enter base A: "))
        bBase=float(input("Enter base B: "))
        height=float(input("Enter height: "))
        areaTrapezoid=areaOfTrapezoid(aBase,bBase,height)
        print("Area of triangle is: {} {}.²".format(areaTrapezoid,unit))
    elif (option==5):
        showTitle()
        radius=float(input("Enter radius: "))
        circleLength=circumference(radius)
        print("Length of circle is: {} {}.²".format(circleLength,unit))
    elif (option==6):
        showTitle()
        radiusC=float(input("Enter radius: "))
        areaC=areaCircle(radius)
        print("Area of circle is: {} {}²".format(areaC,unit))
    elif (option==7):
        while True: 
            factNum=float(input("Enter a number to find its factorial: "))
            if (factNum<=0):
                break
            print("Error, invalid value. Enter a positive number.")        
        factorialOfNum=factorial(factNum)
        print("Factorial of {} is: ".format(factNum,factorialOfNum))
    else:
        break

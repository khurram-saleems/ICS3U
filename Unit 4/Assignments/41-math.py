#     Assignment | Assignment 3-1
#  Program Title | Math Helper
#                |
#     Written by | Khurram Shaikh
#           Date | Thursday, October 24, 2022
#                |
#    Description | This program incorporates several math
#                | formulas/functions to assist the user.
#                | Asks the user to choose a formula/
#                | function, and performs it given the 
#                | values. Program continues to run until
#                | user exits.

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

def getUnits():
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

def pythag(a,b):
    """Calculate and return sideC of a 
    right-angled triangle, given sideA
    and sideB.

    Arguments:
        a: length of side a
        b: length of side b

    Returns:
        Length of hypotenuse.
    """
    c=math.sqrt(a^2+b^2)
    return c

def quadFormula(a,b,c):
    """Calculate and display zeros of a quadratic relation.

    Arguments: 
        a: coefficient of standard form equation
        b: b value of equation
        c: constant value of equation
    """
    d=(b**2)-(4*a*c)
    if (d>0):   
        print("({:.2f},0) and ({:.2f},0) are the zeros.".format((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a)))
    elif (d==0):
        print(-b/(2*a))
    else:
        print("No zeros in quadratic relation.")

def calcAreaTrap(a,b,h):
    """Calculate and return area of trapezoid,
    given bases value and height.

    Arguments:
        a: value of first base
        b: value of second base
        h: height of trapezoid
    
    Returns: 
        Area of trapezoid.
    """
    A=((a+b)/2)*h
    return A

def calcCircumference(r):
    """Calculate and return circumference,
    given the radius.

    Arguments:
        r: radius of circle
    
    Returns: 
        Circumference of circle.
    """
    c=2*math.pi*r
    return c

def CalcareaCircle(r):
    """Calculate and return area of circle,
    given the radius.

    Arguments:
        r: radius of circle
    
    Returns: 
        Area of circle.
    """
    A=math.pi(r**2)
    return A

def factorial(n):
    """Calculate and return factorial of a number,
    given the user's number.

    Arguments:
        n: user's number to factorial
    
    Returns: 
        Factorial of number.
    """
    return math.factorial(n)
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
    unit=getUnits()
    
    # Start infinite loop in case user enters invalid value
    while True:
        
        # Ask user to select a formula
        option=int(input("Choose a formula: "))
        
        # If option is not between 1 and 8
        # Display error message
        if (option>=1 and option<=8):
            break
        print("Error, select an option between 1 and 8.")
    
    # If option is 1
    if (option==1):
        showTitle()
        
        # Ask user to enter base 
        triangleBase=float(input("Enter base: "))
        
        # Ask user for height 
        triangleHeight=float(input("Enter height: "))
        
        # Call function to calculate and save area of triangle
        areaTriangle=areaOfTriangle(triangleBase,triangleHeight)
        
        # Display area of triangle
        print("Area of the triangle is: {} {}².".format(areaTriangle,unit))
    
    # Else if option is 2
    elif (option==2):
        showTitle()
        
        # Ask user for side A
        sideA=float(input("Enter side A value: "))
        
        # Ask user for side B
        sideB=float(input("Enter side B value: "))
        
        # Call function to calculate length of hypotenuse
        sideC=pythag(sideA,sideB)
        
        # Display length of side C
        print("Length of side C is: {} {}.".format(sideC,unit))
    
    # Else if option is 3
    elif (option==3):
        showTitle()

        # Ask user for A, B, and C value of standard form equation
        aVal=float(input("Enter A value: "))
        bVal=float(input("Enter B value: "))
        cVal=float(input("Enter C value: "))
        
        # Call function and pass in A, B, and C values
        quadFormula(aVal,bVal,cVal)
    
    # Else if option is 4
    elif (option==4):
        showTitle()
        
        # Ask for bases and height of trapezoid
        aBase=float(input("Enter base A: "))
        bBase=float(input("Enter base B: "))
        trapezoidHeight=float(input("Enter height: "))
        
        # Call function to calculate trapezoid area 
        # Pass in base values and height
        areaTrapezoid=calcAreaTrap(aBase,bBase,trapezoidHeight)
        
        # Display area of trapezoid
        print("Area of trapezoid is: {} {}.²".format(areaTrapezoid,unit))
    
    # Else if option is 5
    elif (option==5):
        showTitle()
        
        # Ask user for radius
        circumferenceRadius=float(input("Enter radius: "))
        
        # Call function calculate circumference
        # Pass in radius
        circleLength=calcCircumference(circumferenceRadius)
        
        # Display length of circle
        print("Length of circle is: {} {}.".format(circleLength,unit))
    
    # Else if option is 6
    elif (option==6):
        showTitle()
        
        # Ask user for radius
        circleRadius=float(input("Enter radius: "))
        
        # Call function to calculate area of circle  
        # Pass in radius
        circleArea=CalcareaCircle(circleRadius)
        
        # Display area of circle
        print("Area of circle is: {} {}²".format(circleArea,unit))
    
    # Else if option is 7
    elif (option==7):
        
        # Start infinite loop in case user enters invalid value
        while True: 
            
            # Ask user for number to factorial
            factNum=int(input("Enter a number to find its factorial: "))
            
            # If number is negative 
            # Display error message
            if (factNum>=0):
                break
            print("Error, invalid value. To factorial a number it must be positive.")        
        
        # Call function to get factorial and pass in user's number
        factorialOfNum=factorial(factNum)
        
        # Display factorial of number
        print("Factorial of {} is: {}".format(factNum,factorialOfNum))
    
    # Else exit program
    else:
        break
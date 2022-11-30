#     Assignment | Assignment 4-2
#  Program Title | Fencing Frenzy!
#                |
#     Written by | Khurram Shaikh
#           Date | Wednesday, November 30, 2022
#                |
#    Description | This program assists farmers with mathematical 
#                | operations needed to fence their crops. User
#                | is asked to enter positive dimensions, area
#                | and perimeter are  then calculated and summed. 
#                | Program continues to run until user exits.

def validLenWid(question):
    """Ask user for length/width and validate
    if it is greater than or equal to 0, given
    the question.

    Arguments:
        question: Prompt to ask the user, either length or width.
    
    Returns:
        Valid value of asked dimension.
    """
    while True:
        val=int(input(question))
        if (val>=0):
            break
        print("Error, invalid dimension! Enter a positive number.\n")
    return val

def calcArea(len,wid):
    """Calculate and return area of land fenced
    given the length and width.

    Arguments:
        length: length of one dimension
        width: width of one dimension
    
    Returns:
        Area of land fenced.
    """
    a=len*wid
    print("{:>10} {} m²".format("Area:",a))
    return a

def calcPerim(len,wid):
    """Calculate and return perimeter of fencing
    given the length and width.

    Arguments:
        length: length of one dimension
        width: width of one dimension
    
    Returns:
        Perimeter of fencing.
    """
    p=(len+wid)*2
    print("Perimeter: {} m\n".format(p))
    return p
sumArea,sumPerimeter=0,0
print("In light of the new Ministry of Farming directive, this software will assist in\nthe calculation of your fence's perimeter and area.\n")

# Start infinite loop 
while True:
    
    # Call function to ask for length
    length=validLenWid("Enter length (0 to exit): ")
    
    # If length is 0 exit loop
    if (length==0):
        break
    
    # Call function to ask for width
    width=validLenWid("Enter width: ")
    
    # Call function to calculate area
    # Add area to sum 
    sumArea+=calcArea(length,width)
    
    # Call function to calculate perimeter 
    # Add perimeter to sum
    sumPerimeter+=calcPerim(length,width)

# Display sum of area and perimeter
print("\nFinalized reports:")
for i in range (len("Finalized reports:")):
    print("-",end="")
print("\n\n{:>24} {:>6d} m²".format("Total of land fenced:",sumArea))
print("{} {:>6d} m".format("Total length of fencing:",sumPerimeter))

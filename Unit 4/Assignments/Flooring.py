#     Assignment | Assignment 4-3
#  Program Title | Flooring Factory!
#                |
#     Written by | Khurram Shaikh
#           Date | Friday, December 2, 2022
#                |
#    Description | This program assists in the calculation of 
#                | flooring estimates for the user. User is 
#                | asked dimensions and a flooring option.
#                | Breakdown of costs are provided. Program
#                | continues to run until user exits.

def getArea():
    """Ask user for length and width, calculate 
    and return area of floor.

    Returns:
        Area of floor.
    """
    len=validDimension("{:>42} ".format("\nEnter length of the room in meters:"))
    wid=validDimension("{:>42} ".format("Enter width of room in meters (0 to exit):"))
    area=len*wid
    return area

def getFloorCost():
    """Ask for type of flooring, and return
    cost per square meter.

    Returns:
        Cost per square meter.
    """
    choice=validOption(1,5)
    print("\nPlease select a type of floor covering below:\n")
    optionFormat="{:<15} {:>15}"
    print("#.",optionFormat.format("Flooring Type","Cost per sq. m."))
    print("1.",optionFormat.format("Low pile carpet","$ 19.75"))
    print("2.",optionFormat.format("Shag rug","$ 11.24"))
    print("3.",optionFormat.format("Parquet","$ 17.15"))
    print("4.",optionFormat.format("Linoleum","$ 10.40"))
    print("5.",optionFormat.format("Hardwood","$ 29.97"))
    if (choice==1):
        costPerSm=19.75
    elif (choice==2):
        costPerSm=11.24
    elif (choice==3):
        costPerSm=17.15
    elif (choice==4):
        costPerSm=10.40
    else:
        costPerSm=29.97
    return costPerSm

def calculateCost(area,costPerSm,roomCount):
    """Calculate and display price for materials,
    labour charge, sub-total, HST, and total. Given
    area and cost per square meter.

    Arguments:
        area: Area of floor.
        costPerSm: Cost per square meter based on flooring type.
        roomCount: Total count of rooms user has claculated

    Returns:
        Total cost of flooring.
    """
    total=((area*costPerSm)+(6.5*area))+(((area*costPerSm)+(6.5*area))*0.13)
    print("\n{:<15} {:12.2f}".format("Material cost:",area*costPerSm))
    print("{:<15} {:12.2f}".format("Labour charge:",6.5*area))
    print("{:<15} {:>12}".format("","---------"))
    print("{:<15} {:12.2f}".format("Sub-total",(area*costPerSm)+(6.5*area)))
    print("{:<15} {:12.2f}".format("       HST",((area*costPerSm)+(6.5*area))*0.13))
    print("{:<15} {:>12}".format("","---------"))
    print("{:<15} {:12.2f}\n".format("TOTAL COST",total))
    print("{:<15} {:12.2f}\n".format("Room Count",roomCount))
    return total

def validDimension(question):
    """Ask user to enter a value, given a question,
    and validate that it is greater than 0.

    Arguments:
        question: Prompt to ask the user.

    Returns:
        Valid dimension value.
    """
    while True:
        val=float(input(question))
        if (val>=0):
            break
        print("Error, invalid dimension! Enter a value greater than 0 ")
    return val

def validOption(lowVal,highVal):
    """Ask user to enter an option, given two numbers
    and validate it is between those two numbers.

    Arguments:
        lowVal: First number to check between.
        highVal: Second number to check between.
    
    Returns: 
        Valid option between arguments.
    """
    while True:
        option=int(input("\nEnter your choice: "))
        if (option>=lowVal and option<=highVal):
            break
        print("Error, invalid value! Enter an option between 1 and 5.")
    return option

#### MAIN PROGRAM ####

finalTotal,roomCount=0,0
print("{:-^80}".format("Home Depot Flooring Factory Software!"))
print("\nWelcome to Home Depot's Flooring Software, we offer assisted calculations for")
print("flooring options in various dimensions!\n")

# Start infinite loop
while True: 
    
    # Call function to calculate area and set as area
    area=getArea()
    
    # If area is 0 exit program
    if (area==0):
        break
    roomCount+=1
    
    # Call function to generate floor cost per square meter
    cstSqMeter=getFloorCost()

    # Call function to display and calculate cost
    # Add total to final total
    finalTotal+=calculateCost(area,cstSqMeter,roomCount)

# If final total is greater than 0
if (finalTotal>0):
    
    # Display final total
    print("{:<15} {:>12}".format("","---------"))
    print("{:<15} {:12.2f}\n".format("FINAL TOTAL",finalTotal))
    print("{:<15} {:12.2f}\n".format("Room Count",roomCount))

# Display parting message
print("Thanks for using the Home Depot Flooring Factory Software!")
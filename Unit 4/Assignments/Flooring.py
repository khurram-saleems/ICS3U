#     Assignment | Assignment 4-3
#  Program Title | Flooring Factory!
#                |
#     Written by | Khurram Shaikh
#           Date | Friday, December 2, 2022
#                |
#    Description | This program 

def getArea():
    len=float(input("Enter length of the room in meters: "))
    wid=float(input("Enter width of room in meters: "))
    area=len*wid
    return area

def getFloorCost():
    choice=int(input("\nEnter your choice: "))
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

def calculateCost(area,costPerSm):
    total=((area*costPerSm)+(6.5*area))+(((area*costPerSm)+(6.5*area))*0.13)
    print("{:<15} {:12.2f}".format("Material cost:",area*costPerSm))
    print("{:<15} {:12.2f}".format("Labour charge:",6.5*area))
    print("{:<15} {:>12}".format("","---------"))
    print("{:<15} {:12.2f}".format("Sub-total",(area*costPerSm)+(6.5*area)))
    print("{:<15} {:12.2f}".format("       HST",((area*costPerSm)+(6.5*area))*0.13))
    print("{:<15} {:>12}".format("","---------"))
    print("{:<15} {:12.2f}".format("TOTAL COST",total))
    return total

#### MAIN PROGRAM ####

finalTotal=0
while True: 
    area=getArea()
    print("Please select a type of floor covering below:\n")
    optionFormat="{:<15} {:>15}"
    print("#.",optionFormat.format("Flooring Type","Cost per sq. m."))
    print("1.",optionFormat.format("Low pile carpet","$ 19.75"))
    print("2.",optionFormat.format("Shag rug","$ 11.24"))
    print("3.",optionFormat.format("Parquet","$ 17.15"))
    print("4.",optionFormat.format("Linoleum","$ 10.40"))
    print("5.",optionFormat.format("Hardwood","$ 29.97"))
    cstSqMeter=getFloorCost()
    finalTotal+=calculateCost(area,cstSqMeter)


while True:
    canadianCitizen=input("Are you a Canadian Citizen? Enter 'Yes' or 'No'? ")
    if (canadianCitizen=="Yes" or canadianCitizen=="No"):
        break
    print("Error! Please enter 'Yes' or 'No'.")
while True:
    positiveNum=int(input("Enter a positive number: "))
    if (positiveNum>=1):
        break
    print("Error! Enter a positive number.")
while True:
    grade=int(input("What grade are you in? "))
    if (grade>=9 and grade<=12):
        break
    print("Error! Enter a highschool grade level between grade 9 and 12!")
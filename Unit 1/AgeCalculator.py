# 07 Practice Programs 2
# Age Calculator
#
# Khurram Shaikh
# Friday, September 23, 2022
#
# Prog Desc

# Import datetime module to see current date
import datetime

# Stores current day date
today=datetime.date.today()

# Stores current year
currentYr=today.year

# Asks user for year of birth
YrOfBirth=int(input("Enter your year of birth: "))

# Subtracts the current year from the user's year of birth
age=currentYr-YrOfBirth
print("You are {} year(s) old.".format(age))
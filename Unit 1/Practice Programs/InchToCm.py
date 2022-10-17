# 07 Practice Programs 2
# Metric Conversion Practice
#
# Khurram Shaikh
# Friday, September 23, 2022
#
# This program asks the user to enter the length of a desk in inches
# and displays the converted value in centimeters.

desk_length=float(input("Enter the length of a desk in inches: "))
desk_cm=2.54*desk_length
print("The length of the desk is {} centimeters.".format(desk_cm))
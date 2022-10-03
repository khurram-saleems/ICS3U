# 05 Displaying Variables
#
# Khurram Shaikh
# Saturday September 24, 2022
#
# This program experiments with the use of variables
# by displaying different statements/equations.

import math

# Multiplies 10 with 15 and displays the answer
num1,num2= 10,15
answer = num1*num2
print("{} X {} = {}.\n".format(num1,num2,answer))

# Displays 15/16 to one decimal place
mark,outOf=15,16
percent= mark/outOf
print("{}/{} = {:.1%}.\n".format(mark,outOf,percent))

# Calculates the average of 75,71,83 and displays to three decimal places
grade1,grade2,grade3=75,71,83
average=(grade1+grade2+grade3)/3
print("Average of {},{},{} is {:.3f}.\n".format(grade1,grade2,grade3,average))

# Saves the name of my favourite course in a variable
course="ICS3U/Intro to Computer Science"
print("My favourite course is {}!\n".format(course))

# Calculates area of circle with a diameter of 12 to one decimal place
diameter=12
radius=diameter/2
area=math.pi*radius**2
print("Area of cirle with diameter of {} and radius of {} is {:.1f} units squared.\n".format(diameter,radius,area))

# Displays the surface area of a sphere with a radius of 15 to 3 decimal places
radius=15
surf_area=4*math.pi*radius**2
print("Total Surface area of a sphere with a radius of {} is {:.3f} units squared.".format(radius,surf_area))
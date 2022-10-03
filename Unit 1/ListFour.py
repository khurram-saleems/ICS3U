# 07 Practice Programs 2
# 
# Khurram Shaikh
# Friday, September 23, 2022
#
# Program displays four numbers in one line, using the 
# .format() method and one without.

# Ask user to enter four numbrers
num1,num2,num3,num4= input("Enter number 1: "),input("Enter number 2: "),input("Enter number 3: "),input("Enter number 4: ")

# Numbers displayed with .format()
print("Numbers entered were: {}, {}, {}, {}.".format(num1,num2,num3,num4))

# Numbers displayed without .format/with comma
print("Numbers entered were:",num1,",",num2,",",num3,",",num4,".")


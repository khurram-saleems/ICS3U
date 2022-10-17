# 10 Practice Programs 2 
# Program 7: Square and Cubes
#
# Khurram Shaikh
# Friday, October 14, 2022
#
# This program outputs a table of numbers to 20 containing
# the numbers, squares, and cubes.

# Displays columns
print("{} {} {}".format("Num","Square","Cube"))

# Start counted loop to 20
for x in range(21):
    
    # Display number, square, and cube
    print("{:2} {:5} {:6}".format(x,x**2,x**3))
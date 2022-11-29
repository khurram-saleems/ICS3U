# 01 Practice Programs 1 
# Program 1: Clear screen and display title
#
# Khurram Shaikh
# Sunday, November 27, 2022
#
# This program clears the screen and displays 
# the title of program underlined. 

def showTitle():
    for i in range(15):
        print()
    print("ShowTitleDemo")
    for x in range(len("ShowTitleDemo")):
        print("=",end="")
    print()
showTitle()
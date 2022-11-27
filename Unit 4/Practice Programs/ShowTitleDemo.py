# 01 Practice Programs 1 
# Program 1: Clear 
#
# Khurram Shaikh
# Sunday, November 27, 2022
#
# This program clears the screen and displays 
# the title of program underlined. 

def showTitle(title):
    for i in range(15):
        print()
    print(title)
    for x in range(len(title)):
        print("=",end="")
    print()
title=input("Enter program title: ")
showTitle(title)
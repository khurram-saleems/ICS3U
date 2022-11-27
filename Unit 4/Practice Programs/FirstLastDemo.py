# 01 Practice Programs 2
# Program 1: First and last letter
#
# Khurram Shaikh
# Sunday, November 27, 2022
#
# This program displays the first and last letter
# of a entered word.

def showFirstLast(word):
    print("{}{}".format(word[0],word[-1]))
while True:
    word=input("Enter a word ('stop' to exit): ")
    if (word=='stop'):
        break
    showFirstLast(word)


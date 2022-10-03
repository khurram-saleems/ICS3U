# 07 Practice Programs 2
# Array Manipulation Practice
#
# Khurram Shaikh
# Friday, September 23, 2022
#
# This program asks user to enter five different items, then reverses the order and displays it. 

# Asks user to enter different items
name,fav_carCompany,favColour,city,fav_num=input("Enter name: "),input("\nEnter favourite car company: "),input("\nEnter favourite colour: "),input("\nEnter your city: "),int(input("\nEnter your favourite whole number: ")) 

# Creates a list containing the user's 5 items
user_items=[name,fav_carCompany,favColour,city,fav_num]

# Reverse's the list
user_items.reverse()

# Displays list in reverse order
print("\nList in reverse order: {}.\n" .format(user_items))

# For loop to iterate through and display array elements
for item in user_items:
    print("-",item)

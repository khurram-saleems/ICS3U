import random 
 
# get player's names 
p1Name=input("Player 1, enter your name: ") 
p2Name=input("Player 2, enter your name: ") 
 
# ask for # of rolls 
totalRolls=int(input("How many rolls of the die? ")) 
 
# set scores to zero 
p1Score = p2Score = 0 
 
print() 
 
# Player 1 plays #################### 
print("Okay {}, your turn to play".format(p1Name)) 
input("Press [Enter]") 
 
# roll the dice totalRolls times, adding roll to score 
for i in range(totalRolls): 
    roll = random.randint(1,6) 
    print(roll,end=" ") 
    p1Score += roll 
 
# display sum 
print() 
print("Your score is:",p1Score) 
 
print() 
 
# Player 2 plays #################### 
print("Okay {}, your turn to play".format(p2Name)) 
input("Press [Enter]") 
 
# roll the dice totalRolls times, adding roll to score 
for i in range(totalRolls): 
    roll = random.randint(1,6) 
    print(roll,end=" ") 
    p2Score += roll 
 
# display sum 
print() 
print("Your score is:",p1Score) 
 
# shows who won 
if (p1Score > p2Score): 
    print("{} won the game!".format(p1Name)) 
elif (p1Score < p2Score): 
    print("{} won the game!".format(p2Name)) 
else: 
    print("Holy same numbers, Batman! It's a tie!") 
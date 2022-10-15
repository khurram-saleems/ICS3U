import random
count=0
while True:
    count+=1
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print("Dice 1: {}, Dice 2: {}".format(dice1,dice2))
    if (dice1 == dice2):
        break
print("\nIt took {} attempts to roll doubles.".format(count))
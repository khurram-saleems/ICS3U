import random    
def diceRoll():
    """Generates two random numbers from 1,6
    and adds them together.
    """

    # Globalize dice1, dice2 and roll
    # to access and modify outside the
    # function  
    dice1,dice2=random.randint(1,6),random.randint(1,6)
    roll=dice1+dice2
    return roll,dice1,dice2
    
x=diceRoll()[0]
y=diceRoll()[1]
z=diceRoll()[2]
print(x)
print(y)
print(z)
# Below contains game that allows user to select the number of dice
# between 1 & 3. Sides of the die can also be selected, when user 
# clicks "Roll Dice" Numbers on each Die randomize.


# below contains random module

import random

# below contains function and loop to randomize the number
def roll_dice(dice, sides):
    roll = []

    for i in range (0, dice):
        face = random.randint(1, sides)
        roll.append(face)

    return roll 

dice = int(input("Dice: "))

#Requires user to pick a number of dice
if (dice <= 0 >= 5):
    print("Can't Play Without a Die; no more than 5 please!")
    quit()

sides = int(input("Sides: "))

#Requires user to pick a number of sides
if sides (sides <= 1 >= 11):
    print("Must have at least one side! But no more than 11 please!")
    quit()


#below performs the action of rolling the dice
roll = roll_dice( dice, sides)

#display results
print(roll)



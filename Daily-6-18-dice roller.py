import random
def dice(n,d):
    total = 0
    for i in range(n):
        total += random.randint(1,d)
    return total

roll = input("Type a dice roll in the form #d#, for example 3d6:  ")

split_roll = roll.split("d")

number_of_dice =int(split_roll[0])
dice_type = int(split_roll[1])
result = dice(number_of_dice,dice_type)
print (result)

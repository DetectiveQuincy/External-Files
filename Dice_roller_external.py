#-----------------------------------------
#  Kenny Coons
# External files with a diceroller
#  Oct.23/19
#-----------------------------------------
#---------------Imports-----------------------
import random
#---------------Functions---------------------
def rolling(repeat):
    total = 0
    for i in range(repeat):
        dice = random.randint(1, 6)
        total = total + dice
    return total
    
# Main Code
play_again = "yes"
while play_again == "yes":
    dice_amount =int(input("how many dice would you like to roll?"))
    player_dice = rolling(dice_amount)
    print("the player got", player_dice)
file = dice_amount + '.txt'
open(file, 'r')
file.append(total)

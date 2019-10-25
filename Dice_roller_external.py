#-----------------------------------------
#  Kenny Coons
# External files with a diceroller
#  Oct.23/19
#-----------------------------------------
#------------Explanation---------------
#The positives of using external files are very expansive. It is near perfect for coding games with
#save games, it can be used to better clean your coding, by essentially “deleting” the extensive lists from
#the program and transferring into external files, and it can also give the player or user
#a significantly  easier way to look at the actual document of what they have, instead of using occasionally hard to read lists.
#they can just opt in and they have the option to call on the contents of the file they want to use.

#There is an extensive amount of uses for external files, from having the ability to  save games,
#to creating and then running lists,You have control your games from "outside" the game, as opposed to having those superfluiois
#print this  and print that, and you will end up much much less lines of code



#---------------Imports-----------------------
import random
#---------------Functions---------------------
def rolling(repeat):
    total = 0
    for i in range(repeat):
        dice = random.randint(1, 6)
        total = total + dice
    return total

def write_highscore(dice_amount, total):
    file = open((str(dice_amount) + '.txt') , 'a')
    file.write(str(total) + '\n')
    file.close()

def read_highscore(dice_amount, total):
    file = open((str(dice_amount) + '.txt') , 'r')
    high_scores = file.readlines
    print(high_scores)
    file.close()
    
    
# Main Code
play_again = "yes"
while play_again == "yes":
    dice_amount =int(input("how many dice would you like to roll?"))
    player_dice = rolling(dice_amount)
    print("the player got", player_dice)
    choice = input("Would you like to play again?").lower()
    if choice == "yes":
        play_again = "yes"
    elif choice == "no":
        play_again = "no"
    else:
        print("Sorry I didn't understand that, try again")
        choice
    write_highscore(dice_amount, player_dice)
    read_highscore(dice_amount, player_dice)



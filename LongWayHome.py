import time
import random
from LongWayHomePlayer import player
from LongWayHomeEnemy import enemy
from LongWayHomeGameBoard import gameBoardCreation


currentPlayer = player()
gameBoardSize =  7
gameMap = gameBoardCreation(gameBoardSize)

battleIntro = ["come crashing out of the forrest, heading straight for you!",
               "enemies appear from the shadows brandishing weapons!",
               "creatures come rushing for you, rabbid with bloodlust!"]

gameOn = True


def sleepertimer(i):
    time.sleep(i)
    return ""


#battle
def battleField():
    battleOn = True

    enemyGroup = []
    
#Adds number of enemies found in current player location to the enemy list.
    for i in range(gameMap.gameBoard[currentPlayer.currentLocation[0]][currentPlayer.currentLocation[1]][0]):
        newEnemy = enemy(random.randint(0,2), random.randint(0,1))
        enemyGroup.append(newEnemy)
        
    print(len(enemyGroup), battleIntro[random.randint(0, len(battleIntro)-1)], "What would you like to do?\n")

    while(battleOn):
        meleeEn = 0
        rangeEn = 0

        for i in enemyGroup:
            if (i.etype == "melee"):
                meleeEn += 1
            elif(i.etype == "range"):
                rangeEn += 1

        if rangeEn > 0 :
            print("%3s%-3s"*rangeEn %("","R"))
        print("")
        if meleeEn > 0 :
            print("%3s%-3s"*meleeEn %("","M"))

        print("\n"*3)

        while (True) :
            battleChoice = int(input("1. Attack - 2. Defend - 3. Run\n"))
            if battleChoice == 1 :
                print("You attack!")
                break
            elif battleChoice == 2 :
                print("You Defend!")
                break
            elif battleChoice == 3 :
                print("Running away!\nReturning the way you came from!")
                currentPlayer.currentLocation = currentPlayer.previousLocation
                break
            else:
                print("Wrong input.")
            

    for i in enemyGroup:
        del i
    


def moveAround():


    print(currentPlayer.currentLocation)
    global gameOn

    while gameOn == True:
        movement = input("What direction would you like to move? North(w)-South(s)-East(d)-West(a)\n")
        print(gameOn)
        print(currentPlayer.currentLocation, gameMap.endZoneSet)
        
        if (currentPlayer.currentLocation == gameMap.endZoneSet):
            gameOn = False
            return
        
        if (movement == "w"):
            if (player.currentLocation[1] == 0) :
                print("Can't go any further north.")
                
            else:
                currentPlayer.previousLocation = currentPlayer.currentLocation
                player.currentLocation[1] = player.currentLocation[1]-1
                
        elif (movement == "s"):
            if (player.currentLocation[1] == gameBoardSize-1) :
                print("Can't go any further south.")
                
            else:
                currentPlayer.previousLocation = currentPlayer.currentLocation
                player.currentLocation[1] = player.currentLocation[1]+1

        elif (movement == "a"):
            if (player.currentLocation[0] == 0) :
                print("Can't go any further west.")

            else:
                currentPlayer.previousLocation = currentPlayer.currentLocation
                player.currentLocation[0] = player.currentLocation[0]-1

        elif (movement == "d"):
            if (player.currentLocation[0] == gameBoardSize-1) :
                print("Can't go any further east.")
                
            else:
                currentPlayer.previousLocation = currentPlayer.currentLocation
                player.currentLocation[0] = player.currentLocation[0]+1
                
        else:
            print("Invalid input")

        if(gameMap.gameBoard[currentPlayer.currentLocation[0]][currentPlayer.currentLocation[1]][0]>0):
            battleField()
            
        if(gameMap.gameBoard[currentPlayer.currentLocation[0]][currentPlayer.currentLocation[1]][1]>0):
            gameOn = True
    

#Startup screen
def game_startscreen():

    start_game = input("Start new game? \nY/N? "+ sleepertimer(1))

    if start_game.lower() == "n" or start_game.lower() == "no":
        print("Awww...")
        
    elif start_game.lower() == "y" or start_game.lower() == "yes" or start_game.lower() == "ye":
        print("Lets get this trek started!")
    else:
        didnt = ["Didn't quite catch that...",
                 "Sorry, not really sure what you mean...",
                 "Is that even a real word?",
                 "I didnt really understand that..."]
        print(didnt[random.randrange(0,len(didnt))])
        
        game_startscreen()



print("****** THE LONG WAY HOME ******" )
              
game_startscreen()
gameMap.gameBoardCreator()
moveAround()
print(gameOn)


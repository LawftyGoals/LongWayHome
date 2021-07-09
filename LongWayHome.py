import time
import random
from LongWayHomePlayer import player
from LongWayHomeEnemy import enemy
from LongWayHomeGameBoard import gameBoardCreation


currentPlayer = player()
gameBoardSize =  7
gameMap = gameBoardCreation(gameBoardSize)

battleIntro = ["vile beasts come crashing out of the forrest, heading straight for you!",
               "enemies appear from the shadows brandishing weapons!",
               "creatures come rushing for you, rabbid with bloodlust!"]
battleIntroS = ["vile beast comes crashing out of the forrest, heading straight for you!",
               "enemy appears from the shadows brandishing its weapons!",
               "creature comes rushing for you, rabbid with bloodlust!"]

gameOn = True


def sleepertimer(i):
    time.sleep(i)
    return ""


#battle
def battleField():
    battleOn = True

    enemyGroup = {}

#Adds number of enemies found in current player location to the enemy list.
    for i in range(gameMap.gameBoard[currentPlayer.currentLocation[0]][currentPlayer.currentLocation[1]][0]):
        newEnemy = enemy(random.randint(0,2), random.randint(0,1))
        newEnemy.numberInGroup = i+1
        enemyGroup.update({newEnemy.numberInGroup : newEnemy})

    if len(enemyGroup) > 1:
        print(len(enemyGroup), battleIntro[random.randint(0, len(battleIntro)-1)], "What would you like to do?\n")
    elif len(enemyGroup) == 0:
        print(len(enemyGroup), battleIntroS[random.randint(0, len(battleIntro)-1)], "What would you like to do?\n")

    while(battleOn):

        if len(enemyGroup) == 0:
            break
        
        meleeEn = 0
        meleeEnGr = []
        rangeEn = 0
        rangeEnGr = []

        for i in enemyGroup:
            if (enemyGroup[i].etype == "melee"):
                meleeEn += 1
                meleeEnGr.append(i)
            elif(enemyGroup[i] == "ranged"):
                rangeEn += 1
                rangeEnGr.append(i)
        print(meleeEnGr)
        print(rangeEnGr)
        
        while (True) :

            if len(enemyGroup) >= 0:
                print("The enemies have been defeated!")
                break

            #enDict = {"space":"", "R" : "R", "M": "M"}
            
            print("\n"*3)

            for ii in enemyGroup :
                if enemyGroup[ii].etype == "ranged":
                    print("   R"+str(enemyGroup[ii].numberInGroup) + "   ", end = "")

            for ii in enemyGroup :
                if enemyGroup[ii].etype == "melee":
                    print("   M"+str(enemyGroup[ii].numberInGroup) + "   ", end = "")
                
            #if rangeEn > 0 :
            #    for i in rangeEnGr :
            #        print("%(space)3s %(R)s" % enDict, end = "")
            #        print(i.numberInGroup, "  ", end = "")
            #print("")
            #if meleeEn > 0 :
            #    for i in meleeEnGr:
            #        print("%(space)2s %(M)s" % enDict, end = "")
            #        print(i.numberInGroup, "  ", end = "")
            
            print("\n"*3)
            if meleeEn > 0:
                print("You must target a melee unit before you can fight the ranged ones.\n")
            
            battleChoice = input("1. Attack - 2. Defend - 3. Run\n")
            if battleChoice == "1" :
                
                while(True) :
                    whatEnemyAttack = int(input("Which enemy do you want to attack?\n"))
                    if whatEnemyAttack <= 0 or whatEnemyAttack > len(enemyGroup) :
                        print("Invalid target")
                    else :
                        #trying to find object by applied value, probably wrong - Was wrong, is being replaced by dictionary search.
                        playerDamage = currentPlayer.strength+(random.randint(-3,5))
                        enemyGroup[whatEnemyAttack].health -= playerDamage
                        print("You attack for %d damage!" %(playerDamage))

                        if enemyGroup[whatEnemyAttack].health <= 0 :
                            del enemyGroup[whatEnemyAttack]
                            print("The target has died!")

                        break
                
                
            elif battleChoice == "2" :
                print("You Defend!")
                break
            elif battleChoice == "3" :
                print("Running away!\nReturning the way you came from!")
                currentPlayer.currentLocation = currentPlayer.previousLocation
                break
            else:
                print("Wrong input.")

            for ii in enemyGroup :
                enemyDamage = enemyGroup[ii].strength+(random.randint(-3,3))
                currentPlayer.health -= enemyDamage
                print("The", enemyGroup[ii].etype, "enemy hurts you for", enemyDamage)
            

    print("You manage to conquer all the enemies!")
    
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


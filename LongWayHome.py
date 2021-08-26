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
    enemyNumberExists = []

#Adds number of enemies found in current player location to the enemy list.
    for i in range(gameMap.gameBoard[currentPlayer.currentLocation[0]][currentPlayer.currentLocation[1]][0]):
        newEnemy = enemy(random.randint(0,2), random.randint(0,1))
        newEnemy.numberInGroup = i+1
        enemyGroup.update({newEnemy.numberInGroup : newEnemy})

    if len(enemyGroup) > 1:
        print(len(enemyGroup), battleIntro[random.randint(0, len(battleIntro)-1)], "What would you like to do?\n")
    elif len(enemyGroup) == 0:
        print(len(enemyGroup), battleIntroS[random.randint(0, len(battleIntro)-1)], "What would you like to do?\n")

    print(len(enemyGroup))

    while(battleOn):

        meleeEn = 0
        meleeEnGr = []
        rangeEn = 0
        rangeEnGr = []

        for i in enemyGroup:
            enemyNumberExists.append(enemyGroup[i].numberInGroup)
            if (enemyGroup[i].etype == "melee"):
                meleeEn += 1
                meleeEnGr.append(i)
            elif(enemyGroup[i] == "ranged"):
                rangeEn += 1
                rangeEnGr.append(i)
        print(meleeEnGr)
        print(rangeEnGr)

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

        battleChoice = input("1. Attack - 2. Defend (and run or riposte)\n")
###ATTACK:
        if battleChoice == "1" :
                
            while(True) :
                whatEnemyAttack = input("Which enemy do you want to attack?\n")
                if whatEnemyAttack.isdigit():
                    if(int(whatEnemyAttack)>0 and int(whatEnemyAttack)<11 and int(whatEnemyAttack) in enemyNumberExists):
                        whatEnemyAttack = int(whatEnemyAttack)
                        break;
                    else:
                        print("Invalid target")
                else:
                    print("Invalid target")
                
            #trying to find object by applied value, probably wrong - Was wrong, is being replaced by dictionary search.
            playerAttackFunction(whatEnemyAttack)
            enemyAttackFunction(-3,3)
###DEFENSE:
                
        elif battleChoice == "2" :
            print("You're on the Defensive!")
            if(len(enemyGroup) > 0):
                for ii in enemyGroup :
                    ##defenseRoll = random.randint(0,99) ## Defense sets 75% chance to miss
                    if(defenseRoll < 25):
                        enemyAttackFunction(-6,0) ## lower damage if in defensive stance.

                    elif(defenseRoll > 24): ## If player defends by 75% it'll be fine and you dodge it. !!!!!!!!!!!!!!!!!Possible to add flavour.
                        print("You manage to dodge the attack!")
                        
                print("You can attempt to disengage and run or attack with a riposte attack!")
                
                runOrRiposte = input("What would you like to do? - 1. Run! 2. Riposte!)
                                     
                if(runOrRiposte == "1"):
                    print("Attempting to run!")
                    time.sleep(1000)
                    chanceOfEscape = random.randint(0,99)
                    if(len(enemyGroup)>5):
                        if(chanceOfEscape > 24):
                            print("You failed to get away!")
                            enemyAttackFunction(-3,3)
                        else:
                            print("You succeeded in escaping!")
                            currentPlayer.currentLocation = currentPlayer.previousLocation
                            break
                    elif(len(enemyGroup)>4):
                        if(chanceOfEscape > 32):
                            print("You failed to get away!")
                            enemyAttackFunction(-3,3)
                        else:
                            print("You succeeded in escaping!")
                            currentPlayer.currentLocation = currentPlayer.previousLocation
                            break
                    elif(len(enemyGroup)>3):
                        if(chanceOfEscape > 49):
                            print("You failed to get away!")
                            enemyAttackFunction(-3,3)
                        else:
                            print("You succeeded in escaping!")
                            currentPlayer.currentLocation = currentPlayer.previousLocation
                            break
                    elif(len(enemyGroup)>2):
                        if(chanceOfEscape > 74):
                            print("You failed to get away!")
                            enemyAttackFunction(-3,3)
                        else:
                            print("You succeeded in escaping!")
                            currentPlayer.currentLocation = currentPlayer.previousLocation
                            break
                    elif(len(enemyGroup)>1):
                        if(chanceOfEscape > 89):
                            print("You failed to get away!")
                            enemyAttackFunction(-3,3)
                        else:
                            print("You succeeded in escaping!")
                            currentPlayer.currentLocation = currentPlayer.previousLocation
                            break
                elif(runOrRiposte == "2"):
                    whatEnemyRiposte = random.randint(0,len(enemyGroup))
                    playerAttackFunction(whatEnemyRiposte)
                    
        else:
            print("Wrong input.")
            

def enemyAttackFunction(attackA,attackB):
    if(len(enemyGroup)>0):
        enemyDamage = enemyGroup[ii].strength+(random.randint(attackA,attackB)) ### Standard attackA -3 attackB 3
        currentPlayer.health -= enemyDamage
        print("The", enemyGroup[ii].etype, "enemy hurts you for", enemyDamage)



def playerAttackFunction(whatEn):
    playerDamage = currentPlayer.strength+(random.randint(-3,5))
    enemyGroup[whatEn].health -= playerDamage
    print("You attack for %d damage!" %(playerDamage))


    if enemyGroup[whatEn].health <= 0 :
        enemyNumberExists.remove(enemyGroup[whatEn].numberInGroup)
        del enemyGroup[whatEn]
        print("The target has died!")
        
        if(len(enemyGroup)<=0):
           print("You have defeated all the enemies!")
           break
        
def foraging(foragingNumbers):
    print("\n"*3)
    if("Foraging" in currentPlayer.spec_abilities):
        currentPlayer.heldResources = currentPlayer.heldResources+foragingNumbers*2
    else:
        currentPlayer.heldResources = currentPlayer.heldResources+foragingNumbers

        
    if numberOfResources == 0:
        print("No resources discovered here.")
    elif(numberOfResources == 1):
        print("You've discovered 1 resource.")
    elif(numberOfResources > 1):
        print("You've discovered", numberOfResources, "resources!")

    selectedChoices=0


    while(True):
        if(selectedChoices==2):
            break
        print("\nNow, what would you like to do?")
        restChoice =input("1. Rest, 2. Heal, 3. Explore, 4. Move on")
        
        if(restChoice == "1"):
            currentPlayer.health = currentPlayer.health+20
            
        elif(restChoice == "2"):
            print("How many resources would you like to use? (Each resource gives 10 health")
            usedResources=input("Amount: ")
            print("Player healed for", usedResources*10, "HP")
            currentPlayer.health = currentPlayer.health+(10*usedResources)

        elif(restChoice == "3"):
            print("Exploring!")
            time.sleep(1000)
            print("...")
            time.sleep(1000)
            possibleExplore()

        elif(restChoice == "4"):
            print("Moving on!")
            break

        else:
            print("Invalid Input")
            
    
    
def possibleExplore():
    


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
            foraging(gameMap.gameBoard[currentPlayer.currentLocation[0]][currentPlayer.currentLocation[1]][1]>0)
    

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


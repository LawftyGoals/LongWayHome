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
endingLines = ["The last enemy attack makes it through your defense, and strikes true. You feel yourself go weak, your sight goes black and your long way home comes up short."]

defenseLines = ["goes all out, but you dodge the attack!"]

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
        newEnemy.etypeI = newEnemy.etypeI+str(newEnemy.numberInGroup)
        enemyGroup.update({newEnemy.numberInGroup : newEnemy})

    if len(enemyGroup) > 1:
        print(len(enemyGroup), battleIntro[random.randint(0, len(battleIntro)-1)], "What would you like to do?\n")
    elif len(enemyGroup) == 1:
        print(len(enemyGroup), battleIntroS[random.randint(0, len(battleIntro)-1)], "What would you like to do?\n")

    print(len(enemyGroup))
    for i in enemyGroup:
        enemyNumberExists.append(enemyGroup[i].numberInGroup)

    while(battleOn):

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
        print("HP:", currentPlayer.health)
        print(enemyNumberExists)
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
            playerAttackFunction(enemyGroup,enemyNumberExists,whatEnemyAttack)
            if(len(enemyGroup)<=0):
               print("You have defeated all the enemies!")
               gameMap.gameBoard[currentPlayer.currentLocation[0]][currentPlayer.currentLocation[1]][0]=0
               break
            for ii in enemyGroup :
                enemyAttackFunction(enemyGroup,ii,-3,3)
###DEFENSE:
                
        elif battleChoice == "2" :
            print("You're on the Defensive!")
            if(len(enemyGroup) > 0):
                for ii in enemyGroup :
                    defenseRoll = random.randint(0,99) ## Defense sets 75% chance to miss
                    if(defenseRoll < 25):
                        enemyAttackFunction(enemyGroup,ii,-8,-3) ## lower damage if in defensive stance.
                        if(currentPlayer.health <= 0):
                            print(endingLines[random.randint(0,len(endingLines)-1)])
                    elif(defenseRoll > 24): ## If player defends by 75% it'll be fine and you dodge it. !!!!!!!!!!!!!!!!!Possible to add flavour.
                        print(enemyGroup[ii].etypeI, defenseLines[random.randint(0,len(defenseLines)-1)])
                        
                print("You can attempt to disengage and run or attack with a riposte attack!")
                
                runOrRiposte = input("What would you like to do? - 1. Run! 2. Riposte!")
                                     
                if(runOrRiposte == "1"):
                    print("Attempting to run!")
                    time.sleep(1)
                    chanceOfEscape = random.randint(0,99)
                    if(len(enemyGroup)>4):
                        if(chanceOfEscape > 24):
                            print("You failed to get away!")
                            enemyAttackFunction(enemyGroup,(random.randint(0,len(enemyNumberExists))-1),-3,3)
                        else:
                            print("You succeeded in escaping!")
                            currentPlayer.currentLocation = currentPlayer.previousLocation
                            break
                    elif(len(enemyGroup)>3):
                        if(chanceOfEscape > 32):
                            print("You failed to get away!")
                            enemyAttackFunction(enemyGroup,(random.randint(0,len(enemyNumberExists))-1),-3,3)
                        else:
                            print("You succeeded in escaping!")
                            currentPlayer.currentLocation = currentPlayer.previousLocation
                            break
                    elif(len(enemyGroup)>2):
                        if(chanceOfEscape > 49):
                            print("You failed to get away!")
                            enemyAttackFunction(enemyGroup,(random.randint(0,len(enemyNumberExists))-1),-3,3)
                        else:
                            print("You succeeded in escaping!")
                            currentPlayer.currentLocation = currentPlayer.previousLocation
                            break
                    elif(len(enemyGroup)>1):
                        if(chanceOfEscape > 74):
                            print("You failed to get away!")
                            enemyAttackFunction(enemyGroup,(random.randint(0,len(enemyNumberExists))-1),-3,3)
                        else:
                            print("You succeeded in escaping!")
                            currentPlayer.currentLocation = currentPlayer.previousLocation
                            break
                    elif(len(enemyGroup)>0):
                        if(chanceOfEscape > 89):
                            print("You failed to get away!")
                            enemyAttackFunction(enemyGroup,(random.randint(0,len(enemyNumberExists))-1),-3,3)
                        else:
                            print("You succeeded in escaping!")
                            currentPlayer.currentLocation = currentPlayer.previousLocation
                            break
                elif(runOrRiposte == "2"):
                    whatEnemyRiposte = random.randint(0,len(enemyNumberExists)-1)
                    playerAttackFunction(enemyGroup,enemyNumberExists, enemyNumberExists[whatEnemyRiposte])
                    if(len(enemyGroup)<=0):
                        gameMap.gameBoard[currentPlayer.currentLocation[0]][currentPlayer.currentLocation[1]][0]
                        print("You have defeated all the enemies!")
                        break
                    
        else:
            print("Wrong input.")
            

def enemyAttackFunction(enemyGroup,ii,attackA,attackB):
    if(len(enemyGroup)>0):
        enemyDamage = enemyGroup[ii].strength+(random.randint(attackA,attackB)) ### Standard attackA -3 attackB 3
        currentPlayer.health -= enemyDamage
        print("The", enemyGroup[ii].etypeI, "enemy hurts you for", enemyDamage)



def playerAttackFunction(enemyGroup,enemyNumberExists, whatEn):
    playerDamage = currentPlayer.strength+(random.randint(-3,5))
    enemyGroup[whatEn].health -= playerDamage
    print("You attack", enemyGroup[whatEn].etypeI, "for %d damage!" %(playerDamage))


    if enemyGroup[whatEn].health <= 0 :
        enemyNumberExists.remove(enemyGroup[whatEn].numberInGroup)
        del enemyGroup[whatEn]
        print("The target has died!")
        
        
def foraging(foragingNumbers):
    print("\n"*3)
    if("Foraging" in currentPlayer.spec_abilities):
        currentPlayer.heldResources = currentPlayer.heldResources+foragingNumbers*2
    else:
        currentPlayer.heldResources = currentPlayer.heldResources+foragingNumbers

        
    if foragingNumbers == 0:
        print("No resources discovered here.")
    elif(foragingNumbers == 1):
        print("You've discovered 1 resource.")
    elif(foragingNumbers > 1):
        print("You've discovered", foragingNumbers, "resources!")

    gameMap.gameBoard[currentPlayer.currentLocation[0]][currentPlayer.currentLocation[1]][1]=0

    selectedChoices=0


    while(True):
        if(selectedChoices==2):
            break
        print("\nNow, what would you like to do?")
        print("HP:", currentPlayer.health)
        restChoice =input("1. Rest, 2. Heal, 3. Explore, 4. Move on\n")
        
        if(restChoice == "1"):
            print("You make a camp and tucker down for some rest and relaxation.")
            if(currentPlayer.health < (currentPlayer.maxHealth-currentPlayer.restStrength)) :
                currentPlayer.health = currentPlayer.health+currentPlayer.restStrength
            elif(currentPlayer.health > (currentPlayer.maxHealth-currentPlayer.restStrength)):
                currentPlayer.health = currentPlayer.health+(currentPlayer.maxHealth-currentPlayer.health)
            selectedChoices+=1
            
        elif(restChoice == "2"):
            print("How many resources would you like to use? (Each resource gives 10 health")
            usedResources=input("Amount: ")
            if(usedResources.isdigit()):
                usedResources=int(usedResources)
                if(usedResources <= currentPlayer.heldResources):
                    usedResources=int(usedResources)
                    print("Player healed for", usedResources*10, "HP")
                    currentPlayer.health = currentPlayer.health+(10*usedResources)
                    currentPlayer.heldResources = currentPlayer.heldResources-usedResources
                elif(usedResources>currentPlayer.heldResources):
                    print("You don't have enough resources!")
                elif(usedResources<1):
                    print("Invalid number")
            else:
                print("Invalid input")
            selectedChoices+=1

        elif(restChoice == "3"):
            print("Exploring!")
            time.sleep(1)
            print("...")
            time.sleep(1)
            possibleExplore()
            trackHome()
            selectedChoices+=1

        elif(restChoice == "4"):
            print("Moving on!")
            break

        else:
            print("Invalid Input")
            
    
    
def possibleExplore():
    ##
    print("exploring")
    
def trackHome():
    ##Looks at current palyer location, then at finish location and gives general direction.
        currentPlayerX= currentPlayer.currentLocation[0]
        currentPlayerY= currentPlayer.currentLocation[1]
        endZoneLocationX= gameMap.endZoneSet[0]
        endZoneLocationY= gameMap.endZoneSet[1]

        directionX = endZoneLocationX-currentPlayerX
        directionY = endZoneLocationY-currentPlayerY

        if directionX > 0 and directionY > 0 :
            print("You must go South-East")

        elif directionX < 0 and directionY > 0 :
            print("You must go North-East")

        elif directionX < 0 and directionY < 0 :
            print("You must go North-West")

        elif directionX > 0 and directionY < 0 :
            print("You must go South-West")        

        elif directionX == 0 and directionY > 0 :
            print("You must go East")

        elif directionX < 0 and directionY == 0 :
            print("You must go North")

        elif directionX == 0 and directionY < 0 :
            print("You must go West")

        elif directionX > 0 and directionY == 0 :
            print("You must go South")   


def moveAround():

    print(currentPlayer.currentLocation)
    global gameOn

    while gameOn == True:
        
        print(gameOn)
        print(currentPlayer.currentLocation, gameMap.endZoneSet)

        while(True):
            movement = input("What direction would you like to move? North(w)-South(s)-East(d)-West(a)\n")
            if (movement == "w"):
                if (player.currentLocation[1] == 0) :
                    print("Can't go any further north.")
                    
                else:
                    currentPlayer.previousLocation = currentPlayer.currentLocation
                    player.currentLocation[1] = player.currentLocation[1]-1
                    break
                    
            elif (movement == "s"):
                if (player.currentLocation[1] == gameBoardSize-1) :
                    print("Can't go any further south.")
                    
                else:
                    currentPlayer.previousLocation = currentPlayer.currentLocation
                    player.currentLocation[1] = player.currentLocation[1]+1
                    break

            elif (movement == "a"):
                if (player.currentLocation[0] == 0) :
                    print("Can't go any further west.")

                else:
                    currentPlayer.previousLocation = currentPlayer.currentLocation
                    player.currentLocation[0] = player.currentLocation[0]-1
                    break

            elif (movement == "d"):
                if (player.currentLocation[0] == gameBoardSize-1) :
                    print("Can't go any further east.")
                    
                else:
                    currentPlayer.previousLocation = currentPlayer.currentLocation
                    player.currentLocation[0] = player.currentLocation[0]+1
                    break
                    
            else:
                print("Invalid input")

        if(currentPlayer.currentLocation == gameMap.endZoneSet):
            print("You have reached the end of your journey...")
            break

        if(gameMap.gameBoard[currentPlayer.currentLocation[0]][currentPlayer.currentLocation[1]][0]>0):
            battleField()
            
        #if(gameMap.gameBoard[currentPlayer.currentLocation[0]][currentPlayer.currentLocation[1]][1]>0): ### removed because foraging should happen anyway
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

def endGame():
    print("game ending")

print("****** THE LONG WAY HOME ******" )
              
game_startscreen()
gameMap.gameBoardCreator()
moveAround()
endGame()
print(gameOn)


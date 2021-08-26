import random

class gameBoardCreation:

    def __init__(self, sized):
        self.setSize = sized
        self.gameBoard = []
        self.endZoneSet =[]


    #makes gameboard, endZoneSet is used to randomize the final destination.
    
    def gameBoardCreator(self):

        gameBoardSize = self.setSize

        self.endZoneSet = [random.randint(int(gameBoardSize/2), gameBoardSize-1), random.randint(int(gameBoardSize/2), gameBoardSize-1)]

        print("endzone", self.endZoneSet)
        
        endZoneAttempts= [gameBoardSize/2,gameBoardSize/2]

        for i in range(gameBoardSize):
            self.gameBoard.append([])
            for ii in range(15):
                if(i == 0 and ii == 0):
                    self.gameBoard[i].append([0,0,0])
                    
                elif ([i,ii] == self.endZoneSet):
                    self.gameBoard[i].append([0,0,1])
                    
                elif (i >= (gameBoardSize/2) and ii >=(gameBoardSize/2)):
                    enemyPresent = random.randint(0,5)
                    foodPresent = random.randint(0,2)
                    self.gameBoard[i].append([enemyPresent,foodPresent,0])
                    
                else:
                    enemyPresent = random.randint(0,3)
                    foodPresent = random.randint(0,5)
                    self.gameBoard[i].append([enemyPresent,foodPresent,0])
        

    

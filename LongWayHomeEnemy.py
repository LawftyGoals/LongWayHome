class enemy :
    
    etype = ""
    selectedType = ["melee", "ranged"]

    def __init__(self, level, etype):
        self.level = level
        self.levelMultiplyer = [1, 1.5, 2]
        self.etype = self.selectedType[etype]
        self.numberInGroup = 0
        self.etypeI = ""
        
        if self.etype == "melee":
            self.strength = 10 * self.levelMultiplyer[self.level]
            self.health = 15 * self.levelMultiplyer[self.level]
            self.etypeI = "M"
        elif self.etype == "ranged":
            self.strength = 15 * self.levelMultiplyer[self.level]
            self.health = 10 * self.levelMultiplyer[self.level]
            self.etypeI="R"
        

#Converts level to a multiplyer.
    



#variables important for enemy
    
    
    

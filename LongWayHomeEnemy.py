class enemy :
    
    etype = ""
    selectedType = ["melee", "ranged"]

    def __init__(self, level, etype):
        self.level = level
        self.etype = self.selectedType[etype]
        if self.etype == "melee":
            self.strength = 10 * levelMultiplyer[self.level]
            self.health = 15 * levelMultiplyer[self.level]
        elif self.etype == "ranged":
            self.strength = 15 * levelMultiplyer[self.level]
            self.health = 10 * levelMultiplyer[self.level]
        

#Converts level to a multiplyer.
    levelMultiplyer = [1, 1.5, 2]



#variables important for enemy
    
    
    

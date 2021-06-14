class enemy:

    level = 0
    etype = ""
    selectedType = ["melee", "ranged"]

    def __init__(self, level, etype):
        self.level = level
        self.etype = self.selectedType[etype]
        

#Converts level to a multiplyer.
    levelMultiplyer = [1, 1.5, 2]



#variables important for enemy
    health = 15 * levelMultiplyer[level]
    strength = 15 * levelMultiplyer[level]
    
    

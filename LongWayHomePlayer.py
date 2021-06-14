class player():
    #function defining player characteristics
    name = ""
    health = 100
    strength = 15
    agiity = 15
    spec_abilities = []

    currentLocation = [0, 0]
    previousLocation = [0, 0]

    #All possible special abilities that the character can use to perform better
    possible_spec_abilities = {1:["Foraging",1.5], 2:["Stealth",2], 3:["Combat",25]}

    #function returning what benefit is given by spec_ability
    def ability_effect(ability):
        return possible_spec_abilities[ability][1]

    #return name of ability
    def ability_name(ability):
        return possible_spec_abilities[ability][0]

    


#This contains the blueprint of the player


from pokemonList import pkmnList

class Player:
    def __init__(self,name,starterPkmn,badges,numberOfGymDefeated):
        self.name = name
        self.starterPkmn = starterPkmn
        self.badges = badges
        self.numberOfGymDefeated = numberOfGymDefeated

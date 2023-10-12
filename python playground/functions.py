
from Player import Player
from icecream import ic

#contains all the functions
def startGame():
    print("Welcome to the world of Pokemon!")
    print("My name is Professor Oak!")
    print("This pokemon is named 'Eevee'")
    playerName = input("May I know your name?\n")
    print(f"So, you're {playerName}? Welcome!")
    print("Since you are new, I will give you the chance to choose your own pokemon!")
    print("Choose your own pokemon below:")
    print("------------------------------")
    print("1 - Bulbasaur")
    print("2 - Squirtle")
    print("3 - Charmander")
    print("------------------------------")
    pkmnChosen = input("Enter the number of choice:\n")

   
    if(pkmnChosen == '1'):
        print("You chose Bulbasaur! Great choice!")
    elif(pkmnChosen == '2'):
        print("You chose Squirtle! Great choice!")

    elif(pkmnChosen == '3'):
        print("You chose Charmander! Great choice!")
    else:
        print("Invalid input! Choose correct number range!")



     

    player = Player(playerName,pkmnChosen,0,0)
    ic(player.name)
    ic(player.starterPkmn)
    ic(player.badges)
    ic(player.numberOfGymDefeated)

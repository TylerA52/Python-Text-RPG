from character import *
from battle import *
from utils import *

    # Testing classes/functions for now
battleState = False
exploreState = False
titleState = True

while titleState:
    os.system('clear')
    print("********************************************")
    slow_text("\n          Welome to Text RPG!\n")

    playername = input("What's your name?: ")

    hero = Character(f"{playername}", 1, 100, 30, 20, 5)

    enemy_1 = Character("Goblin", 1, 90, 13, 13, 3)

    hero.stats_screen()

    input("Enter any key to continue...")
    os.system('clear')

    titleState = False
    battleState = True

while battleState:

    battle = Battle(hero, enemy_1)
    battle.run_battle()


from character import *
from battle import *

    # Testing classes/functions for now




running = True

while running:
    print("********************************************")
    print("\n         Welome to Text RPG!")

    playername = input("What's your name?: ")

    hero = Character(f"{playername}", 1, 100, 20, 5)

    enemy_1 = Character("Goblin", 1, 90, 13, 3)

    hero.stats_screen()

    battle = Battle(hero, enemy_1)
    battle.run_battle()


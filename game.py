from character import *
from battle import *
from utils import *

    # Testing classes/functions for now

running = True

while running:
    print("********************************************")
    slow_text("\n          Welome to Text RPG!\n")

    playername = input("What's your name?: ")

    hero = Character(f"{playername}", 1, 100, 20, 5)

    enemy_1 = Character("Goblin", 1, 90, 13, 3)

    hero.stats_screen()

    battle = Battle(hero, enemy_1)
    battle.run_battle()


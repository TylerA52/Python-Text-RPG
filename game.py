from character import *
from battle import *
from utils import *
from explore import *

    # Testing classes/functions for now
battleState = False
exploreState = False
titleState = True

world_map = [
    ["Forest", "River", "Mountain"],
    ["Village", "Crossroads", "Cave"],
    ["Plains", "Ruins", "Castle"]
]

exploration = Explore(world_map)

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
    exploreState = True

while exploreState:
    coords, location = exploration.get_current_location()

    exploration.show_map()
    print("Available directions:", exploration.get_directions())
    movement = input("Move where? (n/s/e/w) ").lower()
    exploration.move(movement)
    
    if location == "Crossroads":
        os.system('clear')
        print("You have encountered a Goblin!")
        exploreState = False
        battleState = True

while battleState:

    battle = Battle(hero, enemy_1)
    battle.run_battle()


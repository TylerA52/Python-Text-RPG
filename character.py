# TO DO: Algorithm for stats and leveling up (hardcoded stats and damage atm)
from utils import *

class Character:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def stats_screen(self):
        print("-----------------------")
        print(f"| Level: {self.level}            |")
        print(f"| Health: {self.health}         |")
        print(f"| Attack: {self.attack}          |")
        print(f"| Defense: {self.defense}          |")
        print("-----------------------\n")


    def attack_action(self, other):
        dmg = self.attack - other.defense

        other.health -= dmg
        print(f"\n{self.name} attacked for {dmg} damage!\n{other.name} HP: {other.health}")

    def cast_spell(self, other):
        print("Which spell?:\n")
        spellChoice = input("Fireball, Ice Shard, Energy Shield: ")
        if spellChoice == "fireball":
            print(f"\n{self.name} casts Fireball!")
            other.health -= 25
        elif spellChoice == "ice shard":
            print(f"\n{self.name} casts Ice Shard!")
            other.health -= 20
        elif spellChoice == "energy shield":
            print(f"\n{self.name} casts Energy Shield!")
            self.defense += 10
        else:
            print("Invalid spell.")
        print(f"\n{other.name} HP: {other.health}")

    def defend(self):
        print(f"{self.name}'s defense increased!")
        self.defense += 2

    def levelup(self):
        self.level += 1
        self.health += 20
        self.attack += 4
        self.defense += 2

        print(f"{self.name} has leveled up!\n\n")
        self.stats_screen()



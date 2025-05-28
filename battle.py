from character import *
from utils import *
import random

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.playerTurn = True
        self.playerdefCount = 0
        self.enemydefcount = 0

    def player_turn(self):
        while self.playerTurn:
            slow_text(f"It is {self.player.name}'s turn!")
            playerChoice = input("Attack / Spell / Defend / Stats: ").strip().lower()

            if playerChoice == "attack":
                self.player.attack_action(self.enemy)
                self.playerTurn = False
            elif playerChoice == "spell":
                self.player.cast_spell(self.enemy)
                self.playerTurn = False
            elif playerChoice == "defend":
                if self.playerdefCount < 3:
                    self.player.defend()
                    self.playerdefCount += 1
                    self.playerTurn = False
                else:
                    slow_text("defense can't go any higher!")
            elif playerChoice == "stats":
                print("\nTyler:\n")
                self.player.stats_screen()
                print(f"\n{self.enemy.name}:")
                self.enemy.stats_screen()
            else:
                print("Invalid Choice")

    def enemy_turn(self):
        while not self.playerTurn:
            slow_text(f"\nIt is {self.enemy.name}'s turn!\n")
            
            enemyAction = random.choice(["attack", "spell", "defend"])

            if enemyAction == "attack":
                self.enemy.attack_action(self.player)
            elif enemyAction == "spell":
                 # add random spell choice for enemy as well
                self.enemy.cast_spell(self.player)
            elif enemyAction == "defend":
                if self.enemydefCount < 3:
                    self.enemy.defend()
                    self.enemydefCount += 1
                else:
                    slow_text("defense can't go any higher")

            self.enemy.attack_action(self.player)
            self.playerTurn = True


    def run_battle(self):
        while self.player.health > 0 and self.enemy.health > 0:
            self.player_turn()
            if self.enemy.health <= 0:
                slow_text(f"{self.enemy.name} has been defeated!")
                break

            self.enemy_turn()
            if self.player.health <= 0:
                slow_text(f"{self.player.name} has been defeated!")
                break






from character import *

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.playerTurn = True

    def player_turn(self):
        while self.playerTurn:
            print(f"It is {self.player.name}'s turn!")
            playerChoice = input("Attack / Spell / Defend / Stats: ").strip().lower()

            if playerChoice == "attack":
                self.player.attack_action(self.enemy)
                self.playerTurn = False
            elif playerChoice == "spell":
                self.player.cast_spell(self.enemy)
                self.playerTurn = False
            elif playerChoice == "defend":
                self.player.defend()
                self.playerTurn = False
            elif playerChoice == "stats":
                self.player.stats_screen()
                self.enemy.stats_screen()
            else:
                print("Invalid Choice")

    def enemy_turn(self):
        while not self.playerTurn:
            print(f"\nIt is {self.enemy.name}'s turn!")
            self.enemy.attack_action(self.player)
            self.playerTurn = True


    def run_battle(self):
        while self.player.health > 0 and self.enemy.health > 0:
            self.player_turn()
            if self.enemy.health <= 0:
                print(f"{self.enemy.name} has been defeated!")
                break

            self.enemy_turn()
            if self.player.health <= 0:
                print(f"{self.player.name} has been defeated!")
                break






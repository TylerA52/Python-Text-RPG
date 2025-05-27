
class Character:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def stats_screen(self):
        print(f"Level: {self.level}\nHealth: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}")


    def attack_action(self, other):
        dmg = self.attack - other.defense

        other.health -= dmg
        print(f"{self.name} attacked for {dmg} damage!\n{other.name} HP: {other.health}")

    def cast_spell(self, other):
        print("Which spell?:\n")
        spellChoice = input("Fireball, Ice Shard, Energy Shield")
        if spellChoice == "fireball":
            print(f"{self.name} casts Fireball!")
            other.health -= 25
        elif spellChoice == "ice shard":
            print(f"{self.name} casts Ice Shard!")
            other.health -= 20
        elif spellChoice == "energy shield":
            print(f"{self.name} casts Energy Shield!")
            self.defense += 10
        else:
            print("Invalid spell.")
        print(f"{other.name} HP: {other.health}")

    def defend(self):
        print(f"{self.name}'s defense increased!")

    def levelup(self):
        self.level += 1
        self.health += 20
        self.attack += 4
        self.defense += 2

        print(f"{self.name} has leveled up!\n\n")
        self.stats_screen()




class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense


    def attack_enemy(self, other):
        dmg = self.attack - other.defense

        other.health -= dmg
        print(f"{self.name} attacked for {dmg} damage!\n{other.name} HP: {other.health}")

    #def spell_attack(self, other, spell):



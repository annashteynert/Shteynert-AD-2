class GameCharacter:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage

    def increase_level(self):
        self.level += 1
        self.health *= 1.1
        self.attack *= 1.1

    def __str__(self):
        return f"{self.name} (Level {self.level}) with {self.health} health, {self.attack} attack and {self.defense} defense"


hero = GameCharacter("Hero", 5, 67, 10, 1)
enemy = GameCharacter("Enemy", 96, 11, 77, 8)

for i in range(3):

    print(f"Round {i + 1}:")
    print(hero)
    print(enemy)
    enemy.take_damage(hero.attack - enemy.defense)
    print(f"{hero.name} hits {enemy.name} for {hero.attack - enemy.defense} damage")
    if enemy.health <= 0:
        print(f"{enemy.name} is defeated!")
        hero.increase_level()
        break

    hero.take_damage(enemy.attack - hero.defense)
    print(f"{enemy.name} hits {hero.name} for {enemy.attack - hero.defense} damage")
    if hero.health <= 0:
        print(f"{hero.name} is defeated!")
        enemy.increase_level()
        break


if hero.health > 0 and enemy.health > 0:
    print("It's a draw!")
elif hero.health > 0:
    print(f"{hero.name} wins!")
else:
    print(f"{enemy.name} wins!")
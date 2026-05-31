import random
import time
from random import randint


class character:
    def __init__(self, name, hp, max_hp, attack_power,):
        self.hp=hp
        self.attack_power=attack_power
        self.name=name
        self.max_hp=max_hp

    def is_alive(self):
        return self.hp>0

    def take_damage(self, amount):
        self.hp-=(amount)
        if self.hp<0:
            self.hp=0

    def heal(self):
        self.hp+=randint(5,20)
        if self.hp > self.max_hp:
            self.hp=self.max_hp
player = character("hero", 100, 100, 20)
enemy = character("slime", 70, 70, 15)



print("===================================")
print("welcome to the forest")
print("===================================")
print("\n===================================")
print(f"a wild {enemy.name} blocks your path!")
print("===================================")

while player.is_alive() and enemy.is_alive():
    if enemy.hp ==0:
        break
    print("\n it is now your turn!")
    choise = input("1) attack\n 2) heal\n")
    if choise=="1":
        damage=randint(player.attack_power-5, player.attack_power+5)
        enemy.take_damage(damage)
        print(f"enemy took {damage} damage enemy hp:{enemy.hp}/{enemy.max_hp}")
    elif choise=="2":
        amount=randint(10,15)
        player.heal(amount)
    elif choise=="end":
        break
    else:
        print("you panicked and stood still")
    if enemy.hp ==0:
        break
    print(f"\n it is now the enemy's turn (enemy hp: {enemy.hp}/{enemy.max_hp})")
    move=randint(1,10)
    if move>5:
        damage=randint(enemy.attack_power-5,enemy.attack_power +5)
        player.take_damage(damage)
        print(f"you took {damage} damage current hp:{player.hp}/{player.max_hp}")
    else:
        enemy.heal()
        print(f"enemy healed! enemy hp now:{enemy.hp}/{enemy.max_hp}")
    #end screeennnn
print("=======================")
print("game over")
print("=======================")
if player.hp>0:
    print("you beat him!")
else:
    print("you lost :(")
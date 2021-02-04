# this code is from a tutorial at https://www.youtube.com/watch?v=Pbs6jQZrZA4, making some modifications
# and using it as a template to develop further functionality
# refactored the fight section to be less repetitive...made opponent act independently of user
# test line

import pygame as pg
import numpy as np
import time
import sys
import random

pg.init()

#win = pg.display.set_mode((800, 600))
#pg.display.set_caption("PokeCopy")

# set sprites and their coordinates
charmander_sprite = pg.image.load("otherImages/charmander.png")
squirtle_sprite = pg.image.load("otherImages/squirtle.png")

sprite_width = 64
sprite_height = 64

user_pokemonX = 200
user_pokemonY = 500

opponent_pokemonX = 400
opponent_pokemonY = 200


# Delay printing
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


# a move class, so combat can be calculated by move type/attributes
class Move:
    def __init__(self, name, type, dmg):
        self.name = name
        self.type = type
        self.dmg = dmg


# create the class
class Pokemon:
    def __init__(self, name, type, moves, EVs, health="================"):
        # save variables as attributes
        self.name = name
        self.type = type
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # health bars

    def fight(self, pokemon2):
        # allowing poke1(self) and poke2 to fight
        print("\n-----POKEMON BATTLE-----")
        print(f"\nGo, {self.name}!")
        print(f"\nYour opponent sent out {pokemon2.name}.")

        # print fight info
        print(f"\n{self.name}")
        print("TYPE/", self.type)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("\nVS")

        print(f"\n{pokemon2.name}")
        print("TYPE/", pokemon2.type)
        print("ATTACK/", pokemon2.attack)
        print("DEFENSE/", pokemon2.defense)

        time.sleep(2)

        def attack(pokemon, move, attacked):
            delay_print(f"\n{pokemon.name} used {move.name}! \n")
            time.sleep(1)
            calculate_damage(pokemon, move, attacked)

        # considering type advantages
        def calculate_damage(attacking_pokemon, move, attacked_pokemon):

            version = ["Fire", "Water", "Grass"]

            for i, k in enumerate(version):
                if move.type == k:

                    # both types the same
                    if attacked_pokemon.type == k:
                        attacked_pokemon.defense *= 1.25
                        print("\nIts not very effective...")

                    # Poke2 is strong
                    if attacked_pokemon.type == version[(i+1) % 3]:
                        attacked_pokemon.defense *= 1.5
                        print("\nIt's not very effective...")

                    # attack is super effective
                    if attacked_pokemon.type == version[(i+2) % 3]:
                        attacked_pokemon.defense *= 0.75
                        print("\nIt's super effective!")

            # determine damage
            attack_damage = attacking_pokemon.attack + move.dmg
            damage_after_defense = attack_damage/attacked_pokemon.defense
            attacked_pokemon.bars -= damage_after_defense
            attacked_pokemon.health = ""

            # add back bars plus defense boost
            for j in range(int(attacked_pokemon.bars)):
                attacked_pokemon.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHEALTH\t{self.bars}")
            print(f"{pokemon2.name}\t\tHEALTH\t{pokemon2.bars}")
            time.sleep(0.5)

        # The fighting begins
        # loop to continue while a pokemon still has health
        while (self.bars > 0) and (pokemon2.bars > 0):
            print(f"{self.name}\t\tHEALTH\t{self.bars}")
            print(f"{pokemon2.name}\t\tHEALTH\t{pokemon2.bars}\n")

            # print the attacks available to your pokemon
            for i, x in enumerate(self.moves):
                move = self.moves[i]
                print(move.name)

            # pick a move and input it to the attack function
            index = int(input("Pick a move. "))
            attack(self, self.moves[index - 1], pokemon2)

            # check if pokemon2 has fainted
            if pokemon2.bars <= 0:
                delay_print("\n..." + pokemon2.name + " fainted.")
                money = np.random.choice(5000)
                delay_print(f"\nOpponent paid you ${money}.")
                break

            # opposing pokemon chooses attacks at random, micro-AI opponent
            index = random.randint(1, 4)
            attack(pokemon2, pokemon2.moves[index - 1], self)

            # check if pokemon1 has fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + " fainted.")
                delay_print("\n Ash whited...")
                break


Ember = Move("Ember", "Fire", 5)
Tackle = Move("Tackle", "Normal", 2)
Bite = Move("Bite", "Normal", 3)
Scratch = Move("Scratch", "Normal", 2)
Bubble = Move("Bubble", "Water", 4)
WaterGun = Move("Water Gun", "Water", 3)
IvyWhip = Move("Ivy Whip", "Grass", 4)

if __name__ == '__main__':
    # create pokemon object
    charmander = Pokemon("Charmander", "Fire",
                         [Ember, Tackle, Bite, Scratch],
                         {"ATTACK": 4, "DEFENSE": 2})
    squirtle = Pokemon("Squirtle", "Water",
                         [Bubble, Scratch, Tackle, Bite],
                         {"ATTACK": 3, "DEFENSE": 3})
    bulbasaur = Pokemon("Bulbasaur", "Grass",
                         [IvyWhip, Scratch, Tackle, Bite],
                         {"ATTACK": 2, "DEFENSE": 5})

    charmander.fight(squirtle)


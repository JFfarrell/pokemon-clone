import pygame as pg
import numpy as np
import time
import sys

# Delay printing


def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


# create the class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health="================"):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # health bars

    def fight(self, pokemon2):
        # allowing poke1(self) and poke2 to fight

        # print fight info
        print("-----POKEMON BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("\nVS")

        print(f"\n{pokemon2.name}")
        print("TYPE/", pokemon2.types)
        print("ATTACK/", pokemon2.attack)
        print("DEFENSE/", pokemon2.defense)
        print("\nVS")

        time.sleep(2)

        # considering type advantages
        version = ["Fire", "Water", "Grass"]
        for i, k in enumerate(version):
            if self.types == k:

                # both types the same
                if pokemon2.types == k:
                    self.defense *= 1.5
                    pokemon2.defense *= 1.5
                    string_1_attack = "\nIts not very effective..."
                    string_2_attack = "\nIts not very effective..."

                # Poke2 is strong
                if pokemon2.types == version[(i+1) % 3]:
                    pokemon2.attack *= 1.5
                    pokemon2.defense *= 1.5
                    string_1_attack = "\nIt's not very effective..."
                    string_2_attack = "\nIt's super effective!"

                # Poke1 is strong
                if pokemon2.types == version[(i+2) % 3]:
                    self.attack *= 1.5
                    self.defense *= 1.5
                    string_1_attack = "\nIt's super effective!"
                    string_2_attack = "\nIt's not very effective..."

        # The fighting begins
        # loop to continue while a pokemon still has health
        while (self.bars > 0) and (pokemon2.bars > 0):
            print(f"{self.name}\t\tHEALTH\t{self.bars}")
            print(f"{pokemon2.name}\t\tHEALTH\t{pokemon2.bars}\n")

            print(f"\nGo, {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)

            index = int(input("Pick a move."))
            delay_print(f"{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # determine damage
            pokemon2.bars -= self.attack
            pokemon2.health = ""

            # add back bars plus defense boost
            for j in range(int(pokemon2.bars + 0.1*pokemon2.defense)):
                pokemon2.health += "="

            time.sleep(1)
            print(f"\n {self.name}\t\tHEALTH\t{self.bars}")
            print(f"\n {pokemon2.name}\t\tHEALTH\t{pokemon2.bars}\n")
            time.sleep(0.5)

            # check if pokemon2 has fainted
            if pokemon2.bars <= 0:
                delay_print("\n..." + pokemon2.name + " fainted.")
                break

            # if poke2 has not fainted, their turn
            for i, x in enumerate(pokemon2.moves):
                print(f"\n{i+1}.", x)

            index = int(input("\nPick a move."))
            delay_print(f"\n{pokemon2.name} used {pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # determine damage
            self.bars -= pokemon2.attack
            self.health = ""

            # add back bars plus defense boost
            for j in range(int(self.bars + .1 * self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"\n{pokemon2.name}\t\tHEALTH\t{pokemon2.bars}")
            print(f"\n{self.name}\t\tHEALTH\t{self.bars}\n")
            time.sleep(0.5)

            # check if pokemon1 has fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + " fainted.")
                break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.")


if __name__ == '__main__':
    # create pokemon object
    charmander = Pokemon("Charmander", "Fire",
                         ["Ember", "Scratch", "Tackle", "Bite"],
                         {"ATTACK" : 4, "DEFENSE" : 2})
    squirtle = Pokemon("Squirtle", "Water",
                         ["Bubble", "Scratch", "Tackle", "Bite"],
                         {"ATTACK": 3, "DEFENSE": 3})
    bulbasaur = Pokemon("Bulbasaur", "Grass",
                         ["Ivy Whip", "Scratch", "Tackle", "Bite"],
                         {"ATTACK": 2, "DEFENSE": 5})

    charmander.fight(squirtle)

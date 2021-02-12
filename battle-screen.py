import pygame as pg
from pygame import mixer
import numpy as np
import time
import sys
import random

pg.init()
pg.mixer.init()

win = pg.display.set_mode((800, 600))
pg.display.set_caption("PokeCopy")

# timer
clock = pg.time.Clock()
current_time = 0
attack_time = 0

# background sound
mixer.music.load("audio/Battle!.mp3")
mixer.music.play(-1)

# background image
battleImage = pg.image.load("otherImages/battlebg.png")
battleBG = pg.transform.scale(battleImage, (800, 600))

# set sprites and their coordinates
original_charmander = pg.image.load("otherImages/charmander.png")
original_squirtle = pg.image.load("otherImages/squirtle.png")
original_bulbasaur = pg.image.load("otherImages/bulbasaur.png")

charmander_sprite = pg.transform.scale(original_charmander, (260, 260))
squirtle_sprite = pg.transform.scale(original_squirtle, (260, 260))
bulbasaur_sprite = pg.transform.scale(original_bulbasaur, (260, 260))

og_charmander_opp = pg.image.load("otherImages/charm_opp.gif")
og_squirtle_opp = pg.image.load("otherImages/squirt_opp.png")
og_bulbasaur_opp = pg.image.load("otherImages/bulb_opp.png")

charmander_opp = pg.transform.scale(og_charmander_opp, (220, 220))
squirtle_opp = pg.transform.scale(og_squirtle_opp, (220, 220))
bulbasaur_opp = pg.transform.scale(og_bulbasaur_opp, (220, 220))

user_pokemonX = 0
user_pokemonY = 350

opponent_pokemonX = 480
opponent_pokemonY = 130

#
health_color = (0, 255, 0)
screen_color = (255, 255, 255)

#
user_health = pg.draw.line(battleBG, health_color, (250, 425), (500, 425), width=6)
opponent_health = pg.draw.line(battleBG, health_color, (250, 175), (500, 175), width=6)

attack = False
attacked = False


def redraw_screen(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2):
    # some animation if an attack happens
    global attack
    global attacked
    while attack:
        reframe(user_pokemon_sprite, opponent_pokemon_sprite, 100, y1, x2, y2)
        pg.time.delay(500)
        attack = False
        reframe(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2)
        pg.time.delay(600)
        attacked = True
    while attacked:
        for x in range(4):
            if x % 2 == 0:
                reframe(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, 4000, y2)
                pg.time.delay(200)
            else:
                reframe(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2)
                pg.time.delay(200)
        attacked = False

    win.blit(battleBG, (0, 0))
    win.blit(user_pokemon_sprite, (x1, y1))
    win.blit(opponent_pokemon_sprite, (x2, y2))
    pg.display.update()


def reframe(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2):
    print(x1)
    win.blit(battleBG, (0, 0))
    win.blit(user_pokemon_sprite, (x1, y1))
    win.blit(opponent_pokemon_sprite, (x2, y2))
    pg.display.update()


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
    def __init__(self, name, sprite, oppSprite, type, moves, EVs, health="================"):
        # save variables as attributes
        self.name = name
        self.sprite = sprite
        self.oppSprite = oppSprite
        self.type = type
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        # health bars
        self.bars = 20


Ember = Move("Ember", "Fire", 5)
Tackle = Move("Tackle", "Normal", 2)
Bite = Move("Bite", "Normal", 3)
Scratch = Move("Scratch", "Normal", 2)
Bubble = Move("Bubble", "Water", 4)
WaterGun = Move("Water Gun", "Water", 3)
IvyWhip = Move("Ivy Whip", "Grass", 4)

if __name__ == '__main__':
    # create pokemon object
    charmander = Pokemon("Charmander", charmander_sprite, charmander_opp, "Fire",
                         [Ember, Tackle, Bite, Scratch],
                         {"ATTACK": 4, "DEFENSE": 2})
    squirtle = Pokemon("Squirtle", squirtle_sprite, squirtle_opp, "Water",
                         [Bubble, Scratch, Tackle, Bite],
                         {"ATTACK": 3, "DEFENSE": 3})
    bulbasaur = Pokemon("Bulbasaur", bulbasaur_sprite, bulbasaur_opp, "Grass",
                         [IvyWhip, Scratch, Tackle, Bite],
                         {"ATTACK": 2, "DEFENSE": 5})

    pokedex = [charmander, squirtle, bulbasaur]

    iChooseYou = int(input("Choose your pokemon (1 = Charmander, 2 = Squirtle, 3 = Bulbasaur: "))
    if iChooseYou <= len(pokedex):
        user = pokedex[iChooseYou - 1]
        random = random.randint(0, 2)
        opponent = pokedex[random]

    running = True

    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        keys = pg.key.get_pressed()

        action = keys[pg.K_LEFT]

        if action:
            attack = True

        redraw_screen(user.sprite, opponent.oppSprite,
                      user_pokemonX, user_pokemonY,
                      opponent_pokemonX, opponent_pokemonY)



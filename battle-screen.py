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

charmander_sprite = pg.transform.scale(original_charmander, (260, 260))
squirtle_sprite = pg.transform.scale(original_squirtle, (260, 260))

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
    #win.blit(health_bar, (550, 50))
    win.blit(user_pokemon_sprite, (x1, y1))
    win.blit(opponent_pokemon_sprite, (x2, y2))
    pg.display.update()


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    current_time = pg.time.get_ticks()

    keys = pg.key.get_pressed()
    action = keys[pg.K_LEFT]

    if action:
        attack = True

    redraw_screen(charmander_sprite, squirtle_sprite, user_pokemonX, user_pokemonY, opponent_pokemonX, opponent_pokemonY)
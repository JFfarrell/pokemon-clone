import pygame as pg
import numpy as np
import time
import sys
import random

pg.init()

win = pg.display.set_mode((800, 600))
pg.display.set_caption("PokeCopy")

# timer
clock = pg.time.Clock()
current_time = 0
attack_time = 0

# set sprites and their coordinates
charmander_sprite = pg.image.load("otherImages/charmander.png")
squirtle_sprite = pg.image.load("otherImages/squirtle.png")

sprite_width = 64
sprite_height = 64

user_pokemonX = 200
user_pokemonY = 500

opponent_pokemonX = 400
opponent_pokemonY = 200

screen_color = (255, 255, 255)

attack = False


def redraw_screen(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2):
    global attack_time
    if attack_time > 500:
        reframe(user_pokemon_sprite, opponent_pokemon_sprite, 250, y1, x2, y2)
        pg.time.wait(1000)
        attack_time = 0

    reframe(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2)


def reframe(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2):
    print(x1)
    win.fill(screen_color)
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
        attack_time = pg.time.get_ticks()
        attack = True

    redraw_screen(charmander_sprite, squirtle_sprite, user_pokemonX, user_pokemonY, opponent_pokemonX, opponent_pokemonY)
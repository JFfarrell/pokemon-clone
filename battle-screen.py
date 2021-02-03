import pygame as pg
import numpy as np
import time
import sys
import random

pg.init()

win = pg.display.set_mode((800, 600))
pg.display.set_caption("PokeCopy")

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

user_poke = charmander_sprite
attack = False


def redraw_screen(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2):
    global attack
    win.fill(screen_color)
    if attack:
        x1 += 40
        win.blit(user_pokemon_sprite, (x1, y1))
        win.blit(opponent_pokemon_sprite, (x2, y2))
        pg.display.update()
        time.sleep(1)
        x1 -= 40
        win.blit(user_pokemon_sprite, (x1, y1))
        win.blit(opponent_pokemon_sprite, (x2, y2))
        pg.display.update()
        attack = False

    win.blit(user_pokemon_sprite, (x1, y1))
    win.blit(opponent_pokemon_sprite, (x2, y2))
    pg.display.update()



running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    action = keys[pg.K_LEFT]

    if action:
        attack = True

    redraw_screen(charmander_sprite, squirtle_sprite, user_pokemonX, user_pokemonY, opponent_pokemonX, opponent_pokemonY)
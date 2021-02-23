import pygame as pg
from pygame import mixer
import time
import sys
import random
import classes

pg.init()
pg.mixer.init()

win = pg.display.set_mode((800, 600))
pg.display.set_caption("PokeCopy")

# background sound
mixer.music.load("audio/Battle!.mp3")

# background image
battleImage = pg.image.load("otherImages/battlebg.png")
battleBG = pg.transform.scale(battleImage, (800, 600))

# set sprites and their coordinates
original_charmander = pg.image.load("otherImages/charmander.png")
original_squirtle = pg.image.load("otherImages/squirtle.png")
original_bulbasaur = pg.image.load("otherImages/bulbasaur.png")

charmander_sprite = pg.transform.scale(original_charmander, (240, 240))
squirtle_sprite = pg.transform.scale(original_squirtle, (240, 240))
bulbasaur_sprite = pg.transform.scale(original_bulbasaur, (240, 240))

og_charmander_opp = pg.image.load("otherImages/charm_opp.gif")
og_squirtle_opp = pg.image.load("otherImages/squirt_opp.png")
og_bulbasaur_opp = pg.image.load("otherImages/bulb_opp.png")

charmander_opp = pg.transform.scale(og_charmander_opp, (220, 220))
squirtle_opp = pg.transform.scale(og_squirtle_opp, (220, 220))
bulbasaur_opp = pg.transform.scale(og_bulbasaur_opp, (220, 220))

user_pokemonX = 0
user_pokemonY = 300

opponent_pokemonX = 480
opponent_pokemonY = 130

# colors
health_color = (0, 255, 0)
screen_color = (255, 255, 255)

# health bars
userBarLength = 750

user_health = pg.draw.line(battleBG, health_color, (550, 425), (userBarLength, 425), width=6)
opponent_health = pg.draw.line(battleBG, health_color, (250, 175), (500, 175), width=6)

# menus and cursors
menu_og = pg.image.load("otherImages/menubox.PNG")
cursor = pg.image.load("otherImages/cursor.png")
myBar_og = pg.image.load("otherImages/myBar.png")
oppBar = pg.image.load("otherImages/oppbar.png")
select_og = pg.image.load("otherImages/select.PNG")
select_menu = pg.image.load("otherImages/demomenu.png")

menu = pg.transform.scale(menu_og, (450, 120))
myBar = pg.transform.scale(myBar_og, (400, 150))
select = pg.transform.scale(select_og, (250, 300))

# menu positions
select_positionX = 200
select_positionY = 200

cursor_positionX = 80
cursor_positionY = 200

battle_menu_cursorX = -120
battle_menu_cursorY = 440

# font
font = pg.font.SysFont('freesansbold.tff', 40)

# choose your menu action
action_choice = 1

# choose your pokemon
choice = 0

attack = False
attacked = False


def pokeAttack(attacker, attacked, move):
    print("Attacked pokemon is: ", attacked.name)
    delay_print(f"{attacker.name} used {move.name}! \n\n")
    calculate_damage(move, attacked)

    # determine damage
    attack_damage = attacker.attack + move.dmg
    damage_after_defense = attack_damage / attacked.defense
    attacked.bars -= damage_after_defense
    attacked.health = ""

    # add back bars plus defense boost
    for j in range(int(attacked.bars)):
        attacked.health += "="

    print(len(attacked.health))
    time.sleep(1)


# considering type advantages
def calculate_damage(move, attacked_pokemon):

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


def redraw_screen(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2):
    # some animation if an attack happens
    global attack
    global attacked
    while attack:
        # send attack information
        pokeAttack(user, opponent, user.moves[action_choice - 1])

        reframe(user_pokemon_sprite, opponent_pokemon_sprite, 100, y1, x2, y2)
        pg.time.delay(500)
        attack = False
        reframe(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2)
        pg.time.delay(500)
        attacked = True

    while attacked:
        for x in range(4):
            if x % 2 == 0:
                reframe(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, 4000, y2)
                pg.time.delay(200)
            else:
                reframe(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2)
                pg.time.delay(200)

        opp_attack(opponent_pokemon_sprite, user_pokemon_sprite, x1, y1, x2, y2)
        attacked = False

    reframe(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2)


def opp_attack(attacked_poke, attacker_poke, x1, y1, x2, y2):
    # some animation if an attack happens
    opponents_attack = random.randint(0, 3)
    time.sleep(2)

    attack = True
    attacked = True

    while attack:
        # send attack information
        pokeAttack(opponent, user, opponent.moves[opponents_attack])

        reframe(attacker_poke, attacked_poke, x1, y1, x2 - 80, y2)
        pg.time.delay(500)
        attack = False
        reframe(attacker_poke, attacked_poke, x1, y1, x2, y2)
        pg.time.delay(500)
        attacked = True

    while attacked:
        for x in range(4):
            if x % 2 == 0:
                reframe(attacker_poke, attacked_poke, 4000, y1, x2, y2)
                pg.time.delay(200)
            else:
                reframe(attacker_poke, attacked_poke, x1, y1, x2, y2)
                pg.time.delay(200)

        attacked = False

    reframe(attacker_poke, attacked_poke, x2, y2, x1, y1)


def reframe(user_pokemon_sprite, opponent_pokemon_sprite, x1, y1, x2, y2):
    win.blit(battleBG, (0, 0))
    win.blit(user_pokemon_sprite, (x1, y1))
    win.blit(opponent_pokemon_sprite, (x2, y2))
    win.blit(menu, (0, 480))
    win.blit(myBar, (400, 348))
    win.blit(oppBar, (180, 140))
    win.blit(cursor, (battle_menu_cursorX, battle_menu_cursorY))
    win.blit(user_atk1, (80, 500))
    win.blit(user_atk2, (260, 500))
    win.blit(user_atk3, (80, 550))
    win.blit(user_atk4, (260, 550))
    win.blit(user_name, (475, 382))
    win.blit(opp_name, (225, 185))
    pg.display.update()


def choice_refresh():
    win.blit(battleBG, (0, 0))
    win.blit(select_menu, (select_positionX, select_positionY))
    win.blit(cursor, (cursor_positionX, cursor_positionY))
    pg.display.update()


# Delay printing
def delay_print(s):
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


Ember = classes.Move("Ember", "Fire", 5)
Tackle = classes.Move("Tackle", "Normal", 2)
Bite = classes.Move("Bite", "Normal", 3)
Scratch = classes.Move("Scratch", "Normal", 2)
Bubble = classes.Move("Bubble", "Water", 4)
WaterGun = classes.Move("Water Gun", "Water", 3)
IvyWhip = classes.Move("Ivy Whip", "Grass", 4)

if __name__ == '__main__':
    # create pokemon object
    charmander = classes.Pokemon("Charmander", charmander_sprite, charmander_opp, "Fire",
                                 [Ember, Tackle, Bite, Scratch],
                                 {"ATTACK": 4, "DEFENSE": 2})
    squirtle = classes.Pokemon("Squirtle", squirtle_sprite, squirtle_opp, "Water",
                               [Bubble, Scratch, Tackle, Bite],
                               {"ATTACK": 3, "DEFENSE": 3})
    bulbasaur = classes.Pokemon("Bulbasaur", bulbasaur_sprite, bulbasaur_opp, "Grass",
                                [IvyWhip, Scratch, Tackle, Bite],
                                {"ATTACK": 2, "DEFENSE": 5})

    pokedex = [charmander, squirtle, bulbasaur]

    choose = True
    while choose:
        screen_color = (0, 255, 0)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                choose = False

            keys = pg.key.get_pressed()
            up = keys[pg.K_UP]
            down = keys[pg.K_DOWN]
            select = keys[pg.K_a]

            if up and cursor_positionY > 200:
                cursor_positionY -= 70
                choice -= 1
            if down and cursor_positionY < 281:
                cursor_positionY += 70
                choice += 1
            if select:
                user = pokedex[choice]
                oppChoice = random.randint(0, 2)
                opponent = pokedex[oppChoice]
                attack1, attack2, attack3, attack4 = user.moves[0], user.moves[1], user.moves[2], user.moves[3]
                user_atk1 = font.render(attack1.name, True, (255, 255, 255))
                user_atk2 = font.render(attack2.name, True, (255, 255, 255))
                user_atk3 = font.render(attack3.name, True, (255, 255, 255))
                user_atk4 = font.render(attack4.name, True, (255, 255, 255))
                user_name = font.render(user.name, True, (0, 0, 0))
                opp_name = font.render(opponent.name, True, (0, 0, 0))

                choose = False

        choice_refresh()

    #mixer.music.play(-1)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    attack = True
                if event.key == pg.K_RIGHT and battle_menu_cursorX < 80:
                    battle_menu_cursorX += 180
                    action_choice += 1
                if event.key == pg.K_LEFT and battle_menu_cursorX > -120:
                    battle_menu_cursorX -= 180
                    action_choice -= 1
                if event.key == pg.K_UP and battle_menu_cursorY > 440:
                    battle_menu_cursorY -= 50
                    action_choice -= 2
                if event.key == pg.K_DOWN and battle_menu_cursorY < 480:
                    battle_menu_cursorY += 50
                    action_choice += 2

        redraw_screen(user.sprite, opponent.oppSprite,
                      user_pokemonX, user_pokemonY,
                      opponent_pokemonX, opponent_pokemonY)




import pygame as pg

pg.init()

win = pg.display.set_mode((800, 600))
pg.display.set_caption("PokeCopy")

# char
walkRight = [pg.image.load('char/r1.png'),
             pg.image.load('char/r2.png'),
             pg.image.load('char/r3.png')]

walkLeft = [pg.image.load('char/l1.PNG'),
            pg.image.load('char/l2.png'),
            pg.image.load('char/l3.png')]

walkToward = [pg.image.load('char/tw1.png'),
              pg.image.load('char/tw2.png'),
              pg.image.load('char/tw3.png')]

walkAway = [pg.image.load('char/aw1.png'),
            pg.image.load('char/aw2.png'),
            pg.image.load('char/aw3.png')]

sprite = pg.image.load('char/aw1.png')

clock = pg.time.Clock()

# character movement
playerX = 390
playerY = 530
width = 64
height = 64
playerX_change = 0
playerY_change = 0
left = False
right = False
up = False
down = False
walkCount = 0

# background
ceruleanSmall = pg.image.load("otherImages/cerulean.png")
cerulean = pg.transform.scale(ceruleanSmall, (1062, 938))
ceruleanX = 0
ceruleanY = 0
ceruleanX_change = 0
ceruleanY_change = 0


def redraw_screen(x, y):
    global walkCount
    global sprite
    win.blit(cerulean, (0, 0))
    if walkCount == 8:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    elif up:
        win.blit(walkAway[walkCount//3], (x, y))
        walkCount += 1
    elif down:
        win.blit(walkToward[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(sprite, (playerX, playerY))
    pg.display.update()


running = True
while running:
    clock.tick(27)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT] and playerX > 40:
            playerY_change = 0
            playerX_change = -2
            print(left, right, up, down)
            left = True
            right = False
            up = False
            down = False
        elif keys[pg.K_RIGHT] and playerX < 550:
            playerY_change = 0
            playerX_change = 2
            print(left, right, up, down)
            right = True
            left = False
            up = False
            down = False
        elif keys[pg.K_UP] and playerY > 20:
            playerX_change = 0
            playerY_change = -2
            right = False
            left = False
            up = True
            down = False
        elif keys[pg.K_DOWN] and playerY > 20:
            playerX_change = 0
            playerY_change = 2
            right = False
            left = False
            up = False
            down = True

        if event.type == pg.KEYUP:
            playerX_change = 0
            playerY_change = 0
            right = False
            left = False
            up = False
            down = False
            walkCount = 0

    playerX += playerX_change
    playerY += playerY_change
    redraw_screen(playerX, playerY)



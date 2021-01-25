import pygame

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PokeCopy")

# char
walkRight = [pygame.image.load('char/r1.png'),
             pygame.image.load('char/r2.png'),
             pygame.image.load('char/r3.png')]

walkLeft = [pygame.image.load('char/l1.PNG'),
            pygame.image.load('char/l2.png'),
            pygame.image.load('char/l3.png')]

sprite = pygame.image.load('char/stand.PNG')

clock = pygame.time.Clock()

playerX = 390
playerY = 540
width = 64
height = 64
playerX_change = 0
playerY_change = 0
left = False
right = False
walkCount = 0

# background
ceruleanSmall = pygame.image.load("otherImages/cerulean.png")
cerulean = pygame.transform.scale(ceruleanSmall, (1062, 938))
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
    else:
        win.blit(sprite, (playerX, playerY))
    pygame.display.update()


running = True
while running:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and playerX > 40:
            playerX_change = -2
            left = True
            right = False
            up = False
            down = False
        elif keys[pygame.K_RIGHT] and playerX < 550:
            playerX_change = 2
            right = True
            left = False
            up = False
            down = False
        elif keys[pygame.K_UP] and playerY > 20:
            playerY_change = -2
            right = False
            left = False
            up = True
            down = False
        elif keys[pygame.K_DOWN] and playerY > 20:
            playerY_change = 2
            right = False
            left = False
            up = False
            down = True

        if event.type == pygame.KEYUP:
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



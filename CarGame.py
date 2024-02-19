import sys
import pygame

from pygame.locals import *
pygame.init()
fps = 60
speed = 1000
fpsClock = pygame.time.Clock()
width, height = 1080, 720
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font('freesansbold.ttf', 32)
grass = (34, 152, 85)
asphalt = (149, 149, 149)
white = (255, 255, 255)
sun = (255, 165, 0)
razmetka = pygame.Surface((4, 50))
razmetka1 = pygame.Surface((4, 60))
razmetka.fill(white)
razmetka1.fill(white)
maincar = pygame.image.load("MainCar.png").convert_alpha()
maincar = pygame.transform.scale(maincar, (120, 100))
tree = pygame.image.load("Tree.png").convert_alpha()
tree = pygame.transform.scale(tree, (120, 120))
screen.fill((51, 153, 255))
xc = 580
yc = 620
x = 538
y1 = 360
y2 = 432
y3 = 504
y4 = 576
y5 = 648
x_tree_1 = 100
x_tree_2 = 280
x_tree_3 = 200
x_tree_4 = 90
x_tree_5 = 270
x_tree_6 = 190
y_tree_1 = 360
y_tree_2 = 560
spd = 1
dt = 0
while True:
    pygame.draw.rect(screen, grass, pygame.Rect(0, 360, 1080, 360))
    pygame.draw.polygon(screen, asphalt, ((490, 360), (330, 720), (750, 720), (590, 360)))
    pygame.draw.circle(screen, sun, (1080, 0), 100)
    pygame.draw.rect(screen, (51, 153, 255), (0, 0, 500, 100))
    speed = font.render('SPEED: ' + str(spd), True, (50, 50, 50), (135, 135, 135))
    distance = font.render('DISTANCE: ' + str(dt // 50), True, (50, 50, 50), (135, 135, 135))
    screen.blit(distance, (0, 0, 1000, 0))
    screen.blit(speed, (0, 32, 1000, 0))
    dt = dt + 1
    y1 = y1 + 1
    if y1 >= 720:
        y1 = 360
    y2 = y2 + 1
    if y2 >= 720:
        y2 = 360
    y3 = y3 + 1
    if y3 >= 720:
        y3 = 360
    y4 = y4 + 1
    if y4 >= 720:
        y4 = 360
    y5 = y5 + 1
    if y5 >= 720:
        y5 = 360
    if y1 < 540:
        screen.blit(razmetka, (x, y1))
    if y1 >= 540:
        screen.blit(razmetka1, (x, y1))
    if y2 < 540:
        screen.blit(razmetka, (x, y2))
    if y2 >= 540:
        screen.blit(razmetka1, (x, y2))
    if y3 < 540:
        screen.blit(razmetka, (x, y3))
    if y3 >= 540:
        screen.blit(razmetka1, (x, y3))
    if y4 < 540:
        screen.blit(razmetka, (x, y4))
    if y4 >= 540:
        screen.blit(razmetka1, (x, y4))
    if y5 < 540:
        screen.blit(razmetka, (x, y5))
    if y5 >= 540:
        screen.blit(razmetka1, (x, y5))
    screen.blit(maincar, (xc, yc))
    y_tree_1 = y_tree_1 + 1
    y_tree_2 = y_tree_2 + 1
    x_tree_1 = x_tree_1 - 0.55
    x_tree_2 = x_tree_2 - 0.55
    x_tree_3 = x_tree_3 - 0.55
    x_tree_4 = x_tree_4 - 0.55
    x_tree_5 = x_tree_5 - 0.55
    x_tree_6 = x_tree_6 - 0.55
    if y_tree_1 >= 790:
        y_tree_1 = 360
        x_tree_1 = 100
        x_tree_2 = 280
        x_tree_3 = 200
    if y_tree_2 >= 790:
        y_tree_2 = 360
        x_tree_4 = 90
        x_tree_5 = 270
        x_tree_6 = 190
    screen.blit(tree, (x_tree_1, y_tree_1))
    screen.blit(tree, (x_tree_2, y_tree_1))
    screen.blit(tree, (x_tree_3, y_tree_1 + 70))
    screen.blit(tree, (x_tree_4, y_tree_2))
    screen.blit(tree, (x_tree_5, y_tree_2))
    screen.blit(tree, (x_tree_6, y_tree_2 + 70))
    screen.blit(tree, (950 - x_tree_1, y_tree_1))
    screen.blit(tree, (950 - x_tree_2, y_tree_1))
    screen.blit(tree, (950 - x_tree_3, y_tree_1 + 70))
    screen.blit(tree, (950 - x_tree_4, y_tree_2))
    screen.blit(tree, (950 - x_tree_5, y_tree_2))
    screen.blit(tree, (950 - x_tree_6, y_tree_2 + 70))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if xc == 580:
                    xc = 380
                else:
                    xc = 580
            if event.key == pygame.K_UP:
                fps = fps + 30
                spd = spd + 1
            if event.key == pygame.K_DOWN:
                if fps > 30:
                    fps = fps - 30
                    spd = spd - 1
    pygame.display.flip()
    fpsClock.tick(fps)

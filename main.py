import pygame
import os 
import random
from modules.classes import *
from modules.mapsetting import map

pygame.init()

backgraunt = pygame.image.load(os.path.join(PATH, 'images/background.png'))
backgraunt = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


x = 0
y = 0
block_list = []

wall_imagel1 = os.path.join(PATH, 'images/wall.png')
wall_imagel2 = os.path.join(PATH, 'images/wall.png')


for i in map:
    for i in row:
        if i == 1:
            block_list.append(block(x, y, 1, wall_imagel1))
        elif i == 2:
            block_list.append(block(x, y, 2, wall_imagel2))
        x += STEP
    y += STEP
    x = 0




is_game_running = True
while is_game_running:
    window.blit(background(0, 0))
    for block in block_lest:
        block.blit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False

    pygame.display.flip()



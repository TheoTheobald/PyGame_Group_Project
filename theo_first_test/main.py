 # -*- coding: utf-8 -*-
"""
Spyder Editor

Level with camera that follows player - attempt 1

This is a temporary script file.
"""
import pygame, sys
from settings import *
from tiles import Tile
from level import Level

pygame.init()
scrn = pygame.display.set_mode((scrnW, scrnH))
clock = pygame.time.Clock()
level = Level(levelLayout, scrn)

#add music from https://freemusicarchive.org/ 
pygame.mixer.music.load("music/bgm1.mp3") # Defrini - The Chonker
pygame.mixer.music.play(loops=-1) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    
       
    scrn.fill('black')
    level.run()
    
    
    pygame.display.update()
    clock.tick(60)

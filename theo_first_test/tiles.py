# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:28:10 2021

Implement tile object

@author: theot
"""

import pygame
from settings import tileSize

class Tile(pygame.sprite.Sprite):
    className = 'tile'
    def __init__(self, pos, size, tType):
        super().__init__()
        img = pygame.image.load(f"images/tile/{tType}.png") # Gets tile image based on passed parameter
        self.image = pygame.transform.scale(img, (tileSize, tileSize))
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self, xShift):
        self.rect.x += xShift
        
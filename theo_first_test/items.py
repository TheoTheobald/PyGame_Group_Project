# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 23:57:10 2021

Items

@author: theot
"""

import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, pos, itemType):
        super().__init__()
        self.pos = pos
        self.type = itemType
        self.image = pygame.image.load(f"images/items/{self.type}.png")
        self.rect = self.image.get_rect(topleft = self.pos)
    
    def update(self, xShift):
        self.rect.x += xShift
        
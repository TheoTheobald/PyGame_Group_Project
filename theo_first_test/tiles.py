# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:28:10 2021

Implement tile object

@author: theot
"""

import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self, xShift):
        self.rect.x += xShift
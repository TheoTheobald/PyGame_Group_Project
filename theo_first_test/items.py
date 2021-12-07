# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 23:57:10 2021

Items

@author: theot
"""

import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, pos):
        pass

class Healthpack(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.className = 'healthpack'
        self.pos = pos
        self.image = pygame.image.load("images/items/healthpack.png")
        self.rect = self.image.get_rect(topleft = self.pos)
        self.healthRestored = 150
        
    def update(self, xShift):
        self.rect.x += xShift
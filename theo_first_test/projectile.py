# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:22:08 2021

Projectiles

@author: theot
"""

import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, thickness, colour, direction, speed): # This is all pretty self explanatory
        super().__init__()
        self.colour = colour
        self.image = pygame.Surface((10, thickness))
        self.image.fill(colour)
        self.rect = self.image.get_rect(center = (x, y))
        self.direction = direction
        self.velocity = speed * direction
            
    def update(self, xShift): # Moves the bullet in the desired direction, taking into account scroll speed
        self.rect.x += self.velocity + xShift
        
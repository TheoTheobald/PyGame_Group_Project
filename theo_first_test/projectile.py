# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:22:08 2021

Projectiles

@author: theot
"""

import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, colour, direction):
        super().__init__()
        self.radius = radius
        self.colour = colour
        self.image = pygame.Surface((10, 5))
        self.image.fill(colour)
        self.rect = self.image.get_rect(center = (x, y))
        self.direction = direction
        self.velocity = 14 * direction
            
    def update(self):
        self.rect.x += self.velocity
        
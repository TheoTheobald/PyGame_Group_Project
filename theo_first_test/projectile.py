# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:22:08 2021

Projectiles

@author: theot
"""

import pygame

class Projectile():
    def __init__(self, x, y, radius, colour, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.direction = direction
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:49:51 2021

Player for the game

@author: theot
"""

from settings import *
from character import Character


class Player(Character):
    className = 'player'

    def __init__(self, pos):
        super().__init__(pos)

        # Player combat
        self.bulletCooldown = 200
        self.bulletColour = GREEN
        self.totalHealth = 500
        self.health = 500

        # Player appearance

    def getInput(self):
        keys = pygame.key.get_pressed()
        if not self.dead:
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.direction.x = 1
                self.facing = 0
                if self.direction.y == 0:
                    self.stance = 1
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.direction.x = -1
                self.facing = 1
                if self.direction.y == 0:
                    self.stance = 1
            else:
                self.direction.x = 0
                self.stance = 0

            if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.direction.y == 0:
                self.jump()

            if keys[pygame.K_SPACE] and self.canShoot:
                self.shooting = True
                self.timeLastShot = pygame.time.get_ticks()
            else:
                self.shooting = False

    def update(self, xShift):
        super().update(xShift)
        self.getInput()




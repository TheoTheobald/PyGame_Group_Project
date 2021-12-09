# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:49:51 2021

All characters for the game

@author: theot
"""

import pygame
from settings import *
from character import Character


class Player(Character):
    className = 'player'

    def __init__(self, pos):
        super().__init__(pos)

        # Player combat
        self.bulletCooldown = 200
        self.bulletColour = GREEN
        self.totalHealth = 9999
        self.health = 9999

        # Player appearance

    def getInput(self):
        keys = pygame.key.get_pressed()
        if not self.dead:
            # Define the horizontal movement
            if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:   
                self.facing = 1                 
                self.direction.x = -1        # Direction -1 is left
                self.stance = 1              # Stance 1 is running
                    
            if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                self.facing = 0
                if self.direction.x:
                    self.rect.x += 1
                self.direction.x = 1
                self.stance = 1
                        
            if not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
                self.direction.x = 0
                self.stance = 0
                
            if keys[pygame.K_a]:    # Face left
                self.facing = 1
                
            if keys[pygame.K_d]:    # Face right
                self.facing = 0
                
            if keys[pygame.K_UP] and self.direction.y == 0: # If not moving vertically - jump
                self.jump()

            if keys[pygame.K_SPACE] and self.canShoot:
                self.shooting = True
                self.timeLastShot = pygame.time.get_ticks()
            else:
                self.shooting = False
            
    def update(self, xShift):
        super().update(xShift)
        self.getInput()







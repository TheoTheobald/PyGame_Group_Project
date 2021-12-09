# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:25:28 2021

Big Enemy

@author: saree
"""
import pygame, os
from character import Character
from settings import *


scrn = pygame.display.set_mode((scrnW, scrnH))

class BigEnemy(Character):
    className = 'bigEnemy'

    def __init__(self, pos):
        super().__init__(pos)
        self.pos = pos
        self.frameIndex = 0
        self.updateTime = pygame.time.get_ticks()
        self.timeLastShot = pygame.time.get_ticks()
        self.getSprites(pos)

        self.totalHealth = 2000
        self.health = 2000
        self.bulletColour = LAVA
        self.bulletCooldown = 1100
        self.bulletThickness = 100
        self.bulletSpeed = 5
        self.bulletOffsetXPlus = 100
        self.bulletOffsetXMinus = 0
        self.bulletOffsetY = 60

    def getSprites(self, pos):
        rightLeft = ['right', 'left']
        for elem in rightLeft:
            frames = len(os.listdir("images/bigEnemy"))
            for i in range(frames):
                img = pygame.image.load(f"images/bigEnemy/{i}.png")
                img = pygame.transform.scale(img, (int(img.get_width() * 2.5), int(img.get_height() * 2.5)))
                if elem == 'right':
                    img = pygame.transform.flip(img, True, False)
                self.animations += [img]
        self.image = self.animations[self.frameIndex]
        self.rect = self.image.get_rect(topleft = pos)

    def animate(self):
        timeGap = 150  # Time waited before resetting image
        f = 0
        if self.facing == 1:
            f = 10
        self.image = self.animations[self.frameIndex + f]  # Update image to match current frame
        if pygame.time.get_ticks() - self.updateTime > timeGap:  # If time since last update has reached timeGap
            self.updateTime = pygame.time.get_ticks()  # Update time since last update to current time
            self.frameIndex += 1  # Move frame forward 1
        if self.frameIndex >= 9:
            self.frameIndex = 0

    def healthBar(self, scrn):
        pygame.draw.rect(scrn, RED, (self.rect.x, self.rect.y - 10, 120, 5))
        pygame.draw.rect(scrn, GREEN, (self.rect.x, self.rect.y - 10, (120 * (self.health/self.totalHealth)), 5))
            
    def update(self, xShift):
        self.rect.x += xShift
        self.animate()
        self.shootRate()
    
            

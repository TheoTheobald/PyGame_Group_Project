# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:25:28 2021

@author: saree
"""

from character import Character
from settings import PURPLE
import pygame, os

class BigEnemy(Character):
    className = 'bigEnemy'
    def __init__(self, pos):
        super().__init__(pos)
        self.pos = pos
        #appearance
        
        
        
        self.bulletCooldown = 400
        self.bulletColour = PURPLE
        
    def getSprites(self, pos):
        self.animations = []
        frames = len(os.listdir("images/bigEnemy"))
        for i in range(frames):
            img = pygame.image.load(f"images/bigEnemy/{i}.png")
            img = pygame.transform.scale(img, (int(img.get_width() * 2.5), int(img.get_height() * 2.5)))
            self.animations += [img]

        self.image = self.animations[self.frameIndex]
        self.rect = self.image.get_rect(topleft = self.pos)

    def animate(self):
        timeGap = 100  # Time waited before resetting image
        self.image = self.animations[self.frameIndex]  # Update image to match current frame
        if pygame.time.get_ticks() - self.updateTime > timeGap:  # If time since last update has reached timeGap
            self.updateTime = pygame.time.get_ticks()  # Update time since last update to current time
            self.frameIndex += 1  # Move frame forward 1
        if self.frameIndex >= len(self.animations):
            self.frameIndex = 0
            
    def update(self, xShift):
        super().__init__(xShift)
        self.animate()
        
        
            

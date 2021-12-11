# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 23:57:10 2021

Items

@author: theot
"""

import pygame, os

class Item(pygame.sprite.Sprite):
    def __init__(self, pos, itemType):
        super().__init__()
        self.pos = pos
        self.type = itemType
        self.image = pygame.image.load(f"images/items/{self.type}.png")
        self.rect = self.image.get_rect(topleft = self.pos)
    
    def update(self, xShift):
        self.rect.x += xShift
        
class Portal(Item):
    def __init__(self, pos, itemType):
        super().__init__(pos, itemType)
        self.frameIndex = 0
        self.getSprites(self.pos)
        self.updateTime = pygame.time.get_ticks()
        
    def getSprites(self, pos):
        self.animations = []
        frames = len(os.listdir("images/items/portal"))
        for i in range(frames):
            img = pygame.image.load(f"images/items/portal/Portal_100x100px{i+1}.png")
            img = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
            self.animations += [img]

        self.image = self.animations[self.frameIndex]
        self.rect = self.image.get_rect(topleft = pos)

    def animate(self):
        timeGap = 100  # Time waited before resetting image
        self.image = self.animations[self.frameIndex]  # Update image to match current frame
        if pygame.time.get_ticks() - self.updateTime > timeGap:  # If time since last update has reached timeGap
            self.updateTime = pygame.time.get_ticks()  # Update time since last update to current time
            self.frameIndex += 1  # Move frame forward 1
        if self.frameIndex >= len(self.animations):
            self.frameIndex = 0
            
    def update(self, xShift):
        self.rect.x += xShift
        self.animate()
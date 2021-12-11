# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:56:09 2021

Boss Enemy

@author: theot
"""
import pygame, os
from settings import *
from character import Character
#from random import randomint


class BossEnemy(Character):
    className = 'boss'
    
    def __init__(self, pos):
        super().__init__(pos)
        self.animations = []
        self.pos = pos
        self.frameIndex = 0
        self.facing = 0
        self.updateTime = pygame.time.get_ticks()
        self.timeLastAttacked = pygame.time.get_ticks()
        self.getSprites(pos)
        self.rect = self.image.get_rect(midbottom=pos)
        #Creating variables for horizontal motion of boss
        self.mean=False #This for ensuring that
        self.criteria=False #This will ensure that boss returns back to orginal starting position
        self.motion_1=True
        self.motion_2=False #To initiate second type of horizontal motion
        self.motion_3=False #To initiate third type of horizontal motion
        self.time_boss_motion=200

        self.totalHealth = 2000
        self.health = 2000
        self.attackCooldown = 500

    def getSprites(self, pos):
        frames = len(os.listdir("images/boss"))
        for i in range(frames):
            img = pygame.image.load(f"images/boss/{i}.png")
            img = pygame.transform.scale(img, (int(img.get_width() * 2.5), int(img.get_height() * 2.5)))
            self.animations += [img]

        self.image = self.animations[self.frameIndex]
        self.rect = self.image.get_rect(topleft=pos)

    def animate(self):
        timeGap = 100  # Time waited before resetting image
        self.image = self.animations[self.frameIndex]  # Update image to match current frame
        if pygame.time.get_ticks() - self.updateTime > timeGap:  # If time since last update has reached timeGap
            self.updateTime = pygame.time.get_ticks()  # Update time since last update to current time
            self.frameIndex += 1  # Move frame forward 1
        if self.frameIndex >= len(self.animations):
            self.frameIndex = 0

    def healthBar(self, scrn):
        pygame.draw.rect(scrn, RED, (self.rect.x, self.rect.y - 10, 120, 5))
        pygame.draw.rect(scrn, GREEN, (self.rect.x, self.rect.y - 10, (120 * (self.health/self.totalHealth)), 5))
            
    def update(self, xShift):
        self.rect.x += xShift
        self.animate()
        #self.boss_collision()
        if  self.motion_1:           #motion_1
            self.horizontal_motion(2)
            self.motion_1=False
            self.motion_2=True
        elif  self.motion_2:           #motion_2
            self.horizontal_motion(5)
            self.motion_3=True
            self.motion_2=False
        elif  self.motion_3:           #motion_3
            self.horizontal_motion(10)
            self.motion_3=False
            self.motion_1=True

    def horizontal_motion(self,speed):
        if not (self.mean):
            if self.rect.midbottom == self.pos and self.criteria:
                return
            self.rect.x -= speed
            if self.rect.left < 0:
                self.mean = True
        else:
            self.rect.x += speed
            if self.rect.x > scrnW - 150:
                self.mean = False
                self.criteria = True


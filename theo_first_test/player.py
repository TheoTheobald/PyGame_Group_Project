# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:49:51 2021

Player for the game

@author: theot
"""

import pygame, os
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.falling = False
        self.facing = 0
        self.frameIndex = 0
        self.updateTime = pygame.time.get_ticks()
        self.stance = 0
        self.shooting = False
        
        
        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 1
        self.jumpSpeed = -20
        
        # Player appearance
        self.animations = []
        rightLeft = ['right', 'left']
        animationTypes = ['Idle', 'Run', 'Jump']
        for j in rightLeft:
            LST = []
            for elem in animationTypes:
                lst = []
                frames = len(os.listdir(f"images/player/{elem}"))
                
                for i in range(frames):
                    img = pygame.image.load(f"images/player/{elem}/{i}.png")
                    img = pygame.transform.scale(img, (int(img.get_width() * 1.5), int(img.get_height() * 1.5)))
                    if j == 'left':
                        img = pygame.transform.flip(img, True, False)
                    lst += [img]
                LST += [lst]
            self.animations += [LST]
             
        self.image = self.animations[self.facing][self.stance][self.frameIndex]
        self.rect = self.image.get_rect(topleft = pos)
        self.bulletColour = pygame.Color(0, 255, 0)
        
    def animatePlayer(self):
        timeGap = 100 # Time waited before resetting image
        self.image = self.animations[self.facing][self.stance][self.frameIndex] # Update image to match current stance and frame
        if pygame.time.get_ticks() - self.updateTime > timeGap: # If time since last update has reached timeGap
            self.updateTime = pygame.time.get_ticks() # Update time since last update
            self.frameIndex += 1                       # Move frame forward 1
        if self.frameIndex >= len(self.animations[self.facing][self.stance]):
            self.frameIndex = 0
        
    def getInput(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing = 0
            if self.direction.y == 0:
                self.stance = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing = 1
            if self.direction.y == 0:
                self.stance = 1
        else:
            self.direction.x = 0
            self.stance = 0
            
        if keys[pygame.K_UP] and self.direction.y == 0:
            self.jump()
            
        if keys[pygame.K_SPACE]:
            self.shooting = True
        else: self.shooting = False
            
    def shoot(self):
        if self.facing == 0:
            Dir = 1
        elif self.facing == 1:
            Dir = -1
        return Projectile(self.rect.x, self.rect.y, 5, self.bulletColour, Dir)

    
    def fall(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def jump(self):
        if not self.falling:
            self.direction.y += self.jumpSpeed
            self.falling = True
            self.frameIndex = 0
            self.stance = 2
            
    def update(self):
        self.getInput()
        self.animatePlayer()
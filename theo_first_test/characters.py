# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 14:49:51 2021

All characters for the game

@author: theot
"""

import pygame, os
from projectile import Projectile
from settings import *

class Character(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        
        # Appearance params
        self.falling = False
        self.facing = 0
        self.frameIndex = 0
        self.animationTimeGap = 100
        self.updateTime = pygame.time.get_ticks()
        self.stance = 0
        self.className = 'character'
        self.getSprites(pos)
        
        # Combat
        self.canShoot = True
        self.shooting = False
        self.timeLastShot = pygame.time.get_ticks()
        self.bulletCooldown = 1000
        self.bulletColour = RED
        self.dead = False

        # Char movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 1
        self.jumpSpeed = -18

    def getSprites(self, pos):
        self.animations = []
        rightLeft = ['right', 'left']
        animationTypes = ['Idle', 'Run', 'Jump', 'Death']
        for j in rightLeft:
            LST = []
            for elem in animationTypes:
                lst = []
                frames = len(os.listdir(f"images/{self.className}/{elem}"))

                for i in range(frames):
                    img = pygame.image.load(f"images/{self.className}/{elem}/{i}.png")
                    img = pygame.transform.scale(img, (int(img.get_width() * 1.5), int(img.get_height() * 1.5)))
                    if j == 'left':
                        img = pygame.transform.flip(img, True, False)
                    lst += [img]
                LST += [lst]
            self.animations += [LST]
        self.image = self.animations[self.facing][self.stance][self.frameIndex]
        self.rect = self.image.get_rect(topleft = pos)
    
    def animatePlayer(self):
        timeGap = 100 # Time waited before resetting image
        self.image = self.animations[self.facing][self.stance][self.frameIndex] # Update image to match current stance and frame
        if pygame.time.get_ticks() - self.updateTime > timeGap: # If time since last update has reached timeGap
            self.updateTime = pygame.time.get_ticks() # Update time since last update
            self.frameIndex += 1                       # Move frame forward 1
        if self.frameIndex >= len(self.animations[self.facing][self.stance]):
            if self.stance == 3:
                self.kill()
            self.frameIndex = 0

    def shoot(self):
        if self.facing == 0:
            Dir = 1
            xPos = self.rect.x + 50
            yPos = self.rect.y + 25
        if self.facing == 1:
            Dir = -1
            xPos = self.rect.x - 10
            yPos = self.rect.y + 25
        return Projectile(xPos, yPos, 5, self.bulletColour, Dir)

    def shootRate(self):
        if self.timeLastShot + self.bulletCooldown < pygame.time.get_ticks() and not self.dead:
            self.canShoot = True
        else:
            self.canShoot = False

    def fall(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if not self.falling:
            self.direction.y += self.jumpSpeed
            self.falling = True
            self.frameIndex = 0
            self.stance = 2
            
    def die(self):
        if self.health <= 0:
            self.dead = True
            self.stance = 3

    def healthBar(self, scrn):
        pygame.draw.rect(scrn, RED, (self.rect.x, self.rect.y - 10, 43, 5))
        pygame.draw.rect(scrn, GREEN, (self.rect.x, self.rect.y - 10, (43 * (self.health/self.totalHealth)), 5))
            
    def update(self):
        self.animatePlayer()
        self.shootRate()
        self.die()


class Player(Character):
    def __init__(self, pos):
        Character.__init__(self, pos)
        self.className = 'player'

        # Player combat
        self.bulletCooldown = 200
        self.bulletColour = GREEN
        self.totalHealth = 50
        self.health = 50

        # Player appearance
        self.getSprites(pos)
        self.image = self.animations[self.facing][self.stance][self.frameIndex]
        self.rect = self.image.get_rect(topleft = pos)

    def getInput(self):
        keys = pygame.key.get_pressed()
        if not self.dead:
            # Define the horizontal movement
            if keys[pygame.K_LEFT]:
                self.direction.x = -1        # Direction -1 is left
                self.stance = 1              # Stance 1 is running   
                self.facing = 1
                    
            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.stance = 1
                self.facing = 0
                    
            if not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
                self.direction.x = 0
                self.stance = 0
                
            if keys[pygame.K_d]:
                self.facing = 0
            if keys[pygame.K_a]:
                self.facing = 1
                          
            if keys[pygame.K_UP] and self.direction.y == 0:
                self.jump()
    
            if keys[pygame.K_SPACE] and self.canShoot:
                self.shooting = True
                self.timeLastShot = pygame.time.get_ticks()
            else: self.shooting = False

    def update(self):
        Character.update(self)
        self.getInput()


class Enemy(Character):
    def __init__(self, pos):
        Character.__init__(self, pos)
        self.totalHealth = 60
        self.health = 60
        self.className = 'enemy'
        self.getSprites(pos)

    def update(self, xShift):
        Character.update(self)
        self.rect.x += xShift

class BossEnemy(Character):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.className = 'boss'
        self.getSprites(pos)
        
        self.totalHealth = 2000
        self.health = 2000
        self.attackCooldown = 500
        
    def update(self, xShift):
        Character.update(self)
        self.rect.x += xShift
        
    def getSprites(self, pos):
        self.animations = []
        frames = len(os.listdir("images/boss"))

        for i in range(frames):
            img = pygame.image.load(f"images/boss/{i}.png")
            img = pygame.transform.scale(img, (int(img.get_width() * 2.5), int(img.get_height() * 2.5)))

            self.animations += [img]
        self.image = self.animations[self.facing][self.stance][self.frameIndex]
        self.rect = self.image.get_rect(topleft = pos)
    
    def animatePlayer(self):
        timeGap = 200 # Time waited before resetting image
        self.image = self.animations[self.facing][self.stance][self.frameIndex] # Update image to match current stance and frame
        if pygame.time.get_ticks() - self.updateTime > timeGap: # If time since last update has reached timeGap
            self.updateTime = pygame.time.get_ticks() # Update time since last update
            self.frameIndex += 1                       # Move frame forward 1
        if self.frameIndex >= len(self.animations[self.facing][self.stance]):
            if self.stance == 3:
                self.kill()
            self.frameIndex = 0
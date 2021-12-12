# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:56:09 2021

Boss Enemy

@author: theot
"""
import pygame, os, random
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
        self.value = 100
        self.stance = 0
        self.getSprites(pos)

        #Creating variables for horizontal motion of boss
        self.speed = 6
        self.mean = False #This for ensuring that it does not stop at starting position after it comes right back again
        #Boss health
        self.totalHealth = 2000
        self.health = 2000
        self.attackCooldown = 1000

    def getSprites(self, pos): # Not ideal to have these functions repeated but since there were different stances and the boss doesn't face a direction
        animationTypes = ['Idle', 'Death'] # it was difficult to factorise out just the common components of the function
        for elem in animationTypes:
            frames = len(os.listdir(f"images/boss/{elem}"))
            lst = []
            for i in range(frames):
                img = pygame.image.load(f"images/boss/{elem}/{i}.png")
                img = pygame.transform.scale(img, (int(img.get_width() * 2.5), int(img.get_height() * 2.5)))
                lst += [img]
            self.animations += [lst]

        self.image = self.animations[self.stance][self.frameIndex]
        self.rect = self.image.get_rect(topleft=pos)

    def animate(self):
        timeGap = 100  # Time waited before resetting image
        self.image = self.animations[self.stance][self.frameIndex]  # Update image to match current frame
        if pygame.time.get_ticks() - self.updateTime > timeGap:  # If time since last update has reached timeGap
            self.updateTime = pygame.time.get_ticks()  # Update time since last update to current time
            self.frameIndex += 1  # Move frame forward 1
        if self.frameIndex >= len(self.animations[self.stance]):
            if self.stance == 1:
                self.kill()
            self.frameIndex = 0

    def healthBar(self, scrn):
        pygame.draw.rect(scrn, RED, (self.rect.x, self.rect.y - 10, 120, 5))
        pygame.draw.rect(scrn, GREEN, (self.rect.x, self.rect.y - 10, (120 * (self.health/self.totalHealth)), 5))

    def horizontalMotion(self): # Governs the bosses movement
        if not self.dead: # Stops movement when dead
            if not (self.mean):
                self.rect.x -= self.speed
                if self.rect.left < 0: # If on left hand side of the wall - change direction and randomise speed
                    pygame.mixer.Channel(1).play(bossMove2)
                    self.speed = random.randint(6, 16)
                    self.mean = True
            else:
                self.rect.x += self.speed
                if self.rect.x > scrnW - self.image.get_width(): # If on right hand side of the wall - change direction and randomise speed
                    pygame.mixer.Channel(0).play(bossMove)
                    self.speed = random.randint(6, 16)
                    self.mean = False


    def update(self, xShift):
        self.rect.x += xShift
        self.animate()
        self.horizontalMotion()
        self.die()


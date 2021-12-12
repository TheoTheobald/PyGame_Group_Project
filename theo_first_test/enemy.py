# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:56:09 2021

Enemy

@author: theot
"""
import pygame.font
import random
from settings import *
from character import Character


class Enemy(Character):
    className = 'enemy'

    def __init__(self, pos, screen):
        super().__init__(pos)
        self.totalHealth = 60
        self.value = 5
        self.health = 60
        self.speaking = False
        self.spoken = False
        self.display = screen
        self.cooldown = 3000
        self.speech = ["Shoot 'em up boys!",
                       "Don't let him get to the boss",
                       "Get him!",
                       "I'll show you!",
                       "How is he so quick!",
                       "Come get some!",
                       "Kill him!",
                       "You might be quick but this bullet is quicker!",
                       "Don't come any closer!",
                       ][random.randint(0, 8)]


    def draw_conversation(self, screen, text, text_colour, bg_colour, pos, size):
        font = pygame.font.SysFont(None, size)
        text = font.render(text, True, text_colour)
        text_rect = text.get_rect(topleft=pos)

        # bg
        bg_rect = text_rect.copy()
        bg_rect.inflate_ip(10, 10)

        # frame
        frame_rect = bg_rect.copy()
        frame_rect.inflate(4, 4)

        pygame.draw.rect(screen, text_colour, frame_rect)
        pygame.draw.rect(screen, bg_colour, bg_rect)
        screen.blit(text, text_rect)

    def showBubble(self, screen):
        if not self.spoken:
            screen.blit(self.image, self.rect.topleft)
            self.draw_conversation(screen, self.speech, (255, 255, 255), (0, 0, 0), self.rect.topright, 25)
            self.last = pygame.time.get_ticks()

    def update(self, xShift, player):
        super().update(xShift)
        if self.rect.x - player.rect.x <= 450 and not self.spoken:
            self.speaking = True

        if self.speaking:
            self.showBubble(self.display)
            now = pygame.time.get_ticks()

            if now - self.last >= self.cooldown:
                self.spoken = True

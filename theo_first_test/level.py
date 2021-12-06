# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:35:59 2021

Level creator

@author: theot
"""
import pygame
from tiles import Tile
from settings import tileSize, scrnW
from player import Player

class Level:
    def __init__(self, levelLayout, scrn):
        self.display = scrn
        self.placeTiles(levelLayout)
        self.bullets = pygame.sprite.Group()
        
        self.scrollSpeed = 0
        
    def placeTiles(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        for rowIndex, row in enumerate(layout):
            for colIndex, cell in enumerate(row):
                x = colIndex * tileSize
                y = rowIndex * tileSize
                if cell == 'X':
                    tile = Tile((x, y), tileSize)
                    self.tiles.add(tile)
                elif cell == 'P':
                    player = Player(((x + tileSize/4), y))
                    self.player.add(player)
                    self.playerActual = player
                    
    def scroll(self):
        player = self.player.sprite
        xPos = player.rect.centerx
        xDir = player.direction.x
        
        if xPos < (scrnW/4) and xDir < 0:
            self.scrollSpeed = 5
            player.speed = 0
        elif xPos > ((3*scrnW)/4) and xDir > 0:
            self.scrollSpeed = -5
            player.speed = 0
        else:
            self.scrollSpeed = 0
            player.speed = 5
    
    def collisionX(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = tile.rect.right
                elif player.direction.x > 0:
                    player.rect.right = tile.rect.left
        
    def collisionY(self):
        player = self.player.sprite
        player.fall()
        
        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top 
                    player.direction.y = 0
                    player.falling = False
                elif player.direction.y < 0:
                    player.rect.top = tile.rect.bottom
                    player.direction.y = 0

        
    def run(self):
        
        
        # Level stuff
        self.tiles.update(self.scrollSpeed)
        self.tiles.draw(self.display)
        self.scroll()
        
        # Player stuff
        self.player.update()
        self.collisionX()
        self.collisionY()
        self.player.draw(self.display)
        
        # Bullet stuff
        self.bullets.draw(self.display)
        self.bullets.update()
        
        if self.playerActual.shooting:
            self.bullets.add(self.playerActual.shoot())
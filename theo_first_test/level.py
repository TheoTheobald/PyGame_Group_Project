# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:35:59 2021

Level creator

@author: theot
"""

import pygame, sys
from tiles import *
from settings import tileSize, scrnW, PURPLE, levelLength
from player import Player
from enemy import Enemy
from bossenemy import BossEnemy
from items import Item

class Level:
    def __init__(self, levelLayout, scrn):
        self.items = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()
        self.display = scrn
        self.placeTiles(levelLayout)
        self.bullets = pygame.sprite.Group()
        self.playerDead = False
        self.scrollSpeed = 0
        self.scrollBG = 0


    def placeTiles(self, layout):
        for rowIndex, row in enumerate(layout):
            for colIndex, cell in enumerate(row):
                x = colIndex * tileSize
                y = rowIndex * tileSize
                if cell == 'X':
                    tile = Tile((x, y), tileSize, cell)
                    self.tiles.add(tile)
                elif cell >= '0' and cell <= '9' or cell == '£' or cell == '$' or cell == '&':
                    tile = Tile((x, y), tileSize, cell)
                    self.tiles.add(tile)
                elif cell == 'P':
                    player = Player(((x + tileSize/4), y + 9))
                    self.player.add(player)
                elif cell == 'E':
                    enemy = Enemy((x, y+10))
                    self.enemies.add(enemy)
                elif cell == 'H':
                    healthpack = Item(((x + tileSize/5), y + 29), 'healthpack')
                    self.items.add(healthpack)
                elif cell == 'J':
                    jumpBoost = Item(((x + tileSize/5), y + 29), 'jumpBoost')
                    self.items.add(jumpBoost)
                elif cell == 'D':
                    dmgBoost = Item(((x + tileSize/5), y + 29), 'dmgBoost')
                    self.items.add(dmgBoost)
                elif cell == 'B':
                    boss = BossEnemy((x - 60, y - 120))
                    self.enemies.add(boss)

    def scroll(self):
        player = self.player.sprite
        xPos = player.rect.centerx
        xDir = player.direction.x
        xPosLeft = player.rect.left
        xPosRight = player.rect.right

        if (xPos < scrnW / 4 and self.scrollBG > abs(5)) and xDir < 0:
            self.scrollSpeed = 5
            player.speed = 0
        elif (xPos > (scrnW * 3 / 4) and self.scrollBG < (levelLength * tileSize) - scrnW) and xDir > 0:
            self.scrollSpeed = -5
            player.speed = 0
        elif xPosLeft + self.scrollSpeed < 0:
            player.speed = 0
        # else:
        #     self.scrollSpeed = 0
        #     player.speed = 5

    def collisionX(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = tile.rect.right
                    player.direction.x = 0
                elif player.direction.x > 0:
                    player.rect.right = tile.rect.left
                    player.direction.x = 0

            for bullet in self.bullets.sprites():
                if tile.rect.colliderect(bullet.rect):
                    bullet.kill()

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
            # for enemy in self.enemies.sprites():
            #     enemy.fall()
            #     if tile.rect.colliderect(enemy.rect):
            #         if enemy.direction.y > 0:
            #             enemy.rect.bottom = tile.rect.top
            #             enemy.direction.y = 0       
            #         elif enemy.direction.y < 0:
            #             enemy.rect.top = tile.rect.bottom
            #             enemy.direction.y = 0
                            
    def bulletHitsCharacter(self):
        player = self.player.sprite

        for bullet in self.bullets.sprites():
            if bullet.rect.colliderect(player.rect):
                bullet.kill()
                player.health -= 10
            for enemy in self.enemies.sprites():
                if bullet.rect.colliderect(enemy.rect) and bullet.colour != enemy.bulletColour and not enemy.dead:
                    enemy.health -= 10
                    if bullet.colour == PURPLE:
                        enemy.health -= 10
                    bullet.kill()

    def pickupItem(self):
        player = self.player.sprite

        for item in self.items.sprites():
            if item.rect.colliderect(player.rect):
                if item.type == 'healthpack':
                    if player.health == player.totalHealth:
                        return
                    player.health += 150
                    if player.health > player.totalHealth:
                        player.health = player.totalHealth
                    item.kill()
                if item.type == 'jumpBoost':
                    player.jumpSpeed -= 6
                    item.kill()
                if item.type == 'dmgBoost':
                    player.bulletColour = PURPLE
                    item.kill()
                        

    def checkPlayerPos(self):
        player = self.player.sprite

        for enemy in self.enemies:
            if enemy.className == 'boss':
                pass
            else:
                if enemy.rect.x > player.rect.x and not enemy.dead:  # Facing left
                    enemy.facing = 1
                if enemy.rect.x < player.rect.x and not enemy.dead:  # Facing right
                    enemy.facing = 0

                if enemy.canShoot:  # Shooting range, height and cooldown
                    if player.rect.y > enemy.rect.y - 50 and player.rect.y < enemy.rect.y + 50:
                        if player.rect.x > enemy.rect.x - 500 and player.rect.x < enemy.rect.x + 500:
                            enemy.shooting = True
                            enemy.timeLastShot = pygame.time.get_ticks()
                else:
                    enemy.shooting = False


    def checkDead(self):
        gameOverFont = pygame.font.SysFont("PT Serif", 60)
        gameOver = gameOverFont.render('YOU DIED - PRESS TO CONTINUE', True, 'red')
        if self.player.sprite.dead:
            self.playerDead = True
        if self.playerDead:
            self.display.blit(gameOver, (200, 300))

    def drawBG(self):
        self.display.fill('black')
        self.scrollBG -= self.scrollSpeed # Background will scroll in an opposite direction of player movement
        bg1 = pygame.image.load('images/background/1.png')
        bg1 = pygame.transform.scale(bg1, (scrnW * 1.5, 768))
        bg2 = pygame.image.load('images/background/2.png')
        bg2 = pygame.transform.scale(bg2, (scrnW * 1.5, 768))
        bg3 = pygame.image.load('images/background/3.png')
        bg3 = pygame.transform.scale(bg3, (scrnW * 1.5, 768))
        bg4 = pygame.image.load('images/background/4.png')
        bg4 = pygame.transform.scale(bg4, (scrnW * 1.5, 768))
        bg5 = pygame.image.load('images/background/5.png')
        bg5 = pygame.transform.scale(bg5, (scrnW * 1.5, 768))
        for x in range (5):
            self.display.blit(bg1, ((x * bg1.get_width() - 100) - self.scrollBG * 0.4, 0))
            self.display.blit(bg2, ((x * bg2.get_width() - 100) - self.scrollBG * 0.5, 0))
            self.display.blit(bg3, ((x * bg3.get_width() - 100) - self.scrollBG * 0.6, 0))
            self.display.blit(bg4, ((x * bg4.get_width() - 100) - self.scrollBG * 0.7, 0))
            self.display.blit(bg5, ((x * bg2.get_width() - 100) - self.scrollBG * 0.8, 0))
    
    
        
        
    def run(self): # This is the part where everything is run - the same as the while loop in most one-page games

        # Level stuff
        self.drawBG()
        self.tiles.update(self.scrollSpeed)
        self.tiles.draw(self.display)
        self.scroll()

        # Items
        self.items.draw(self.display)
        self.pickupItem()
        self.items.update(self.scrollSpeed)

        # Player stuff
        if not self.playerDead:
            self.player.update(self.scrollSpeed)
            self.collisionX()
            self.collisionY()
            self.player.draw(self.display)
            self.player.sprite.healthBar(self.display)
            self.checkDead()

        # Enemy update
        self.enemies.draw(self.display)
        self.enemies.update(self.scrollSpeed)
        self.checkPlayerPos()

        for enemy in self.enemies:
            enemy.healthBar(self.display)

        # Bullet stuff
        self.bullets.draw(self.display)
        self.bullets.update()
        self.bulletHitsCharacter()

        for player in self.player:
            if player.shooting:
                self.bullets.add(player.shoot())
        for enemy in self.enemies:
            if enemy.className != 'boss' and enemy.shooting:
                self.bullets.add(enemy.shoot())

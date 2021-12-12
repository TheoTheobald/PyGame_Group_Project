# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:35:59 2021

Level creator

@author: theot
"""

import pygame, sys
from tiles import *
from settings import *
from player import Player
from enemy import Enemy
from bigEnemy import BigEnemy
from bossenemy import BossEnemy
from items import Item, Portal


class Level:
    def __init__(self, levelLayout, scrn):
        self.items = pygame.sprite.Group() # Creating groups for each of the sprites, tried to group them by what commonly needs to be updated for that sprite type
        self.enemies = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.display = scrn
        self.placeTiles(levelLayout) # Calls the place tiles function to build the level
        self.playerDead = False
        self.levelLength = len(levelLayout[0]) # Gets length of level to help scrolling stop at edge of screen
        self.scrollSpeed = 0 # Initially screen is fixed
        self.scrollBG = 0 # Background is not initially moving
        self.saveScoreCheck = 0

        self.redManDead = False # Checks to see if pre-boss enemy is dead
        self.teleportPlayer = False # True when the player is to be teleported
        self.gameComplete = False # True when the game has been completed

        self.playerBossHit = pygame.time.get_ticks() # prevents player being repeatedly hit by boss - could have been put in boss code tbh

    def placeTiles(self, layout): # Builds the level
        for rowIndex, row in enumerate(layout): # Iterates through the rows and colums of the levelLayout list in settings
            for colIndex, cell in enumerate(row):
                x = colIndex * tileSize
                y = rowIndex * tileSize
                if cell >= '0' and cell <= '9' or cell == '£' or cell == '$' or cell == '&': # Places tiles based on the symbol in the list at that index, and places
                    tile = Tile((x, y), tileSize, cell)                                      # the element at the index*tileSize for x and y
                    self.tiles.add(tile)                                                     # Adds whatever element we have built to its sprite group
                elif cell == 'P':
                    player = Player(((x + tileSize / 4), y + 9))
                    self.player.add(player)
                elif cell == 'E':
                    enemy = Enemy((x, y + 10))
                    self.enemies.add(enemy)
                elif cell == 'H':
                    healthpack = Item(((x + tileSize / 5), y + 29), 'healthpack')
                    self.items.add(healthpack)
                elif cell == 'J':
                    jumpBoost = Item(((x + tileSize / 5), y + 29), 'jumpBoost')
                    self.items.add(jumpBoost)
                elif cell == 'D':
                    dmgBoost = Item(((x + tileSize / 5), y + 29), 'dmgBoost')
                    self.items.add(dmgBoost)
                elif cell == 'Q':
                    portal = Portal((x, y), 'portal')
                    self.items.add(portal)
                elif cell == 'B':
                    boss = BossEnemy((x - 60, y + 90))
                    self.enemies.add(boss)
                elif cell == 'S':
                    bigEnemy = BigEnemy((x - 40, y - 65))
                    self.enemies.add(bigEnemy)

    def scroll(self):
        player = self.player.sprite # Grabs the players sprite for easier referencing
        xPos = player.rect.centerx
        xDir = player.direction.x
        xPosLeft = player.rect.left
        xPosRight = player.rect.right

        if (xPos < scrnW / 3 and self.scrollBG > abs(5)) and xDir < 0: # Scrolls left when in first third of screen
            self.scrollSpeed = 5
            player.speed = 0
        elif (xPos > (scrnW * 2 / 3) and self.scrollBG < (self.levelLength * tileSize) - scrnW) and xDir > 0: # Scrolls right when in final third of screen
            self.scrollSpeed = -5
            player.speed = 0
        elif (xPosLeft + self.scrollSpeed < 0) and xDir < 0: # Stops the player moving at the left most side of the screen
            player.speed = 0
        elif (xPosRight + self.scrollSpeed > scrnW) and xDir > 0: # Stop the player moving at the right most side of the screen
            player.speed = 0
        else:                           # When in middle third player moves as normal
            self.scrollSpeed = 0
            player.speed = 5

    def collisionX(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for tile in self.tiles.sprites():               # Sort of clunky collisions - when there is a tile overlap and the player is moving left
            if tile.rect.colliderect(player.rect):      # affix the players right most point to the left most point of the tile they are colliding with
                if player.direction.x < 0:              # and set their speed in x to 0
                    player.rect.left = tile.rect.right
                    player.direction.x = 0
                elif player.direction.x > 0:            # Then the same in reverse for the left
                    player.rect.right = tile.rect.left
                    player.direction.x = 0

            for bullet in self.bullets.sprites():       # If bullet hits a wall, kill it
                if tile.rect.colliderect(bullet.rect):
                    bullet.kill()

    def collisionY(self):
        player = self.player.sprite
        player.fall()

        for tile in self.tiles.sprites():           # Same logic as x collisions but just for up, down, top and bottom
            if tile.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                    player.direction.y = 0
                    player.falling = False          # Falling boolean prevents a 2nd jump in the air, this allows the player to jump again when they land
                elif player.direction.y < 0:
                    player.rect.top = tile.rect.bottom
                    player.direction.y = 0

    def bulletHitsCharacter(self):
        player = self.player.sprite
        for bullet in self.bullets.sprites():
            if bullet.rect.x > 6000 or bullet.rect.x < 0: # Kills bullets that go too far off the screen - 6000 is probably a tad high
                bullet.kill()
            if bullet.rect.colliderect(player.rect): # If bullet hits player do 10 dmg
                player.health -= 10
                if bullet.colour == LAVA:           # If bullet is from the red dude, do another 10
                    player.health -= 10
                bullet.kill()                       # Kill bullet
            for enemy in self.enemies.sprites():

                if enemy.dead and not enemy.scoreGiven:  # if bullet kills enemy
                    if enemy.className == 'bigEnemy':
                        pygame.mixer.Channel(0).play(bigEnemyDead)
                    else:
                        pygame.mixer.Channel(1).play(enemyHit)
                    player.score += enemy.value  # increment score
                    enemy.scoreGiven = True
                if bullet.rect.colliderect(enemy.rect) and bullet.colour != enemy.bulletColour and not enemy.dead:
                    enemy.health -= 10                      # If bullet hits enemy take 10 hp
                    if bullet.colour == PURPLE:             # If player has bullet upgrade (turns bullets purple) take another 10 hp
                        enemy.health -= 10                  # Kill bullet
                    bullet.kill()
        # display score to screen
        font = pygame.font.Font('fonts/BarcadeNB.otf', 30)
        text_surface = font.render(f"SCORE {player.score}", True, 'white')
        text_rect = text_surface.get_rect()
        text_rect.topleft = (50, 50)
        self.display.blit(text_surface, text_rect)   # Writes the score in the top left of the screen

    def bossCollision(self): # Boss does contact damage rather than shoots bullets
        player = self.player.sprite
        for enemy in self.enemies:
            if enemy.className == 'boss':
                if enemy.rect.colliderect(player.rect) and self.playerBossHit + enemy.attackCooldown < pygame.time.get_ticks():
                    pygame.mixer.Channel(2).play(bossHit) # If boss hits player and hasn't hit player for at least the allotted minimum time between attacks
                    player.health -= 75                     # Take 75 hp
                    self.playerBossHit = pygame.time.get_ticks()    # Reset hit timer

    def redMan(self):
        redDead = True      # Checks to see if the red dude is dead
        for enemy in self.enemies:
            if enemy.className == 'bigEnemy':
                redDead = False
            else:
                pass
        if redDead:
            self.redManDead = True # If he's dead allow teleportation

    def pickupItem(self):
        player = self.player.sprite

        for item in self.items.sprites(): # Function that governs all item pickups
            if item.rect.colliderect(player.rect):
                if item.type == 'healthpack':
                    pygame.mixer.Channel(2).play(getItem)
                    if player.health == player.totalHealth:
                        return
                    player.health += 150
                    if player.health > player.totalHealth: # Basic collision stuff
                        player.health = player.totalHealth
                    item.kill()
                if item.type == 'jumpBoost':
                    pygame.mixer.Channel(2).play(getItem)
                    player.jumpSpeed -= 6
                    item.kill()
                if item.type == 'dmgBoost':
                    pygame.mixer.Channel(2).play(getItem)
                    player.bulletColour = PURPLE
                    item.kill()
                if item.type == 'portal':
                    pygame.mixer.Channel(3).play(portal)    # Portal doesn't exactly belong here but it made more sense than it being a tile
                    if self.redManDead:                     # If the player touches the portal the portal sound plays
                        self.teleportPlayer = True          # If the red man is dead, teleport them, otherwise display message to kill red man
                    else:
                        redDudePromptFont = pygame.font.Font('fonts/BarcadeNB.otf', 30)
                        redDudePrompt = redDudePromptFont.render('I should kill that red thing..', True, 'white')
                        redDudePromptRect = redDudePrompt.get_rect()
                        redDudePromptRect.midtop = (scrnW // 2, 300)
                        self.display.blit(redDudePrompt, redDudePromptRect)

    def checkPlayerPos(self):
        player = self.player.sprite

        for enemy in self.enemies:
            if enemy.className == 'boss': # Stops the boss from trying to change directions as he doesn't face anywhere
                pass
            else:
                if enemy.rect.x + (enemy.image.get_width() / 2) > player.rect.x + (
                        player.image.get_width() / 2) and not enemy.dead:  # Facing left
                    enemy.facing = 1
                if enemy.rect.x - (player.image.get_width() / 2) < player.rect.x - (
                        enemy.image.get_width() / 2) and not enemy.dead:  # Facing right
                    enemy.facing = 0
                if enemy.canShoot and not player.dead:  # Shooting range, height and cooldown
                    if player.rect.y > enemy.rect.y - enemy.image.get_height() and player.rect.y < enemy.rect.y + enemy.image.get_height():
                        if player.rect.x > enemy.rect.x - 500 and player.rect.x < enemy.rect.x + 500:
                            enemy.shooting = True  # Allows the enemy to shoot
                            enemy.timeLastShot = pygame.time.get_ticks()  # Resets the shot timer
                            if enemy.className == 'bigEnemy':
                                pygame.mixer.Channel(4).play(bigEnemyGrowl)
                            else:
                                pygame.mixer.Channel(5).play(enemyGun)
                else:
                    enemy.shooting = False

    def checkDeadOrComplete(self): # Checks to see if the game is over, either from death or completion
        player = self.player.sprite
        gameOverFont = pygame.font.Font('fonts/Barcade.otf', 100)
        scoreFont = pygame.font.Font('fonts/Barcade.otf', 60)
        gameContFont = pygame.font.Font('fonts/BarcadeNB.otf', 40)

        gameOver = gameOverFont.render('YOU DIED', True, 'white')
        gameComp = gameOverFont.render('YOU KILLED THE BOSS', True, 'white')
        gameCont = gameContFont.render('PRESS ENTER TO CONTINUE', True, 'white')
        finalScore = scoreFont.render(f'Your Score is {player.score}', True, 'yellow')

        gameOverRect = gameOver.get_rect()
        gameCompRect = gameComp.get_rect()
        gameContRect = gameCont.get_rect()
        finalScoreRect = finalScore.get_rect()

        gameOverRect.midtop = (scrnW // 2, 200)
        gameCompRect.midtop = (scrnW // 2, 200)
        gameContRect.midtop = (scrnW // 2, 550)
        finalScoreRect.midtop = (scrnW // 2, 350)

        if player.dead or self.gameComplete: # Saves the score to the scores file
            # save score
            if self.saveScoreCheck < 1:
                # append score to file
                with open("theo_first_test_scores.txt", "a") as scoreFile:
                    scoreFile.write(f"{str(player.score)}\n")
                self.saveScoreCheck += 1

            # read high score
            with open("theo_first_test_scores.txt", "r") as scoreFile:
                scores = list(map(int, scoreFile.readlines()))
                player.highScore = max(scores)

            highScoreDisplay = scoreFont.render(f"High score : {player.highScore}", True, "white")
            highScoreRect = highScoreDisplay.get_rect()
            highScoreRect.midtop = (scrnW // 2, 450)

            if player.dead:
                self.display.blit(gameOver, gameOverRect) # Displays relevant message on screen
            else:
                self.display.blit(gameComp, gameCompRect)
            self.display.blit(finalScore, finalScoreRect)
            self.display.blit(highScoreDisplay,highScoreRect)
            self.display.blit(gameCont, gameContRect)


    def drawBG(self):
        self.display.fill('black')
        self.scrollBG -= self.scrollSpeed  # Background will scroll in an opposite direction of player movement
        bg1 = pygame.image.load('images/background/1.png')
        bg1 = pygame.transform.scale(bg1, (scrnW * 1.5, 768))
        bg2 = pygame.image.load('images/background/2.png')
        bg2 = pygame.transform.scale(bg2, (scrnW * 1.5, 768))
        bg3 = pygame.image.load('images/background/3.png')
        bg3 = pygame.transform.scale(bg3, (scrnW * 1.5, 768))
        bg5 = pygame.image.load('images/background/5.png')
        bg5 = pygame.transform.scale(bg5, (scrnW * 1.5, 768))
        for x in range(5):
            self.display.blit(bg1, ((x * bg1.get_width() - 100) - self.scrollBG * 0.4, 0))
            self.display.blit(bg2, ((x * bg2.get_width() - 100) - self.scrollBG * 0.5, 0))
            self.display.blit(bg3, ((x * bg3.get_width() - 100) - self.scrollBG * 0.6, 0))
            self.display.blit(bg5, ((x * bg2.get_width() - 100) - self.scrollBG * 0.8, 0))

    def checkComplete(self): # Checks to see if the game is complete and then allows player to return to menu by changing level boolean
        if self.levelLength < 30:
            bossDead = True
            for enemy in self.enemies:
                if enemy.className == 'boss':
                    bossDead = False
            if bossDead == True:
                self.gameComplete = True


    def run(self):  # This is the part where everything is run - the same as the while loop in most one-page games

        # Level stuff
        self.drawBG()
        self.tiles.update(self.scrollSpeed)
        self.tiles.draw(self.display)
        self.scroll()
        self.redMan()
        self.checkComplete()

        # Items
        self.items.draw(self.display)
        self.pickupItem()
        self.items.update(self.scrollSpeed)

        # Enemy update
        self.enemies.draw(self.display)
        self.enemies.update(self.scrollSpeed)
        self.checkPlayerPos()
        self.bossCollision()

        for enemy in self.enemies:
            enemy.healthBar(self.display)

        # Bullet stuff
        self.bullets.draw(self.display)
        self.bullets.update(self.scrollSpeed)
        self.bulletHitsCharacter()

        for player in self.player:
            if player.shooting:
                self.bullets.add(player.shoot())
        for enemy in self.enemies:
            if enemy.className != 'boss' and enemy.shooting:
                self.bullets.add(enemy.shoot())

        # Player stuff
        if not self.playerDead:
            self.player.update(self.scrollSpeed)
            self.collisionX()
            self.collisionY()
            self.player.draw(self.display)
            self.player.sprite.healthBar(self.display)
            self.checkDeadOrComplete()

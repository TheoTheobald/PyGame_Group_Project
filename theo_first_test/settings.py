# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:22:43 2021

General settings file for game

@author: theot
"""

import pygame
from pygame import mixer

levelLayout = ['989888999988989998898_________________________8989898999898___________',
                '____£___D_____________________E_______E_______8________E_J£___________',
                '____£__536_________E£_______5316______£______________513236___________',
                '____£_________E___5326______9______5316_______£E_E______9_____________',
                '____£________516__________£_8_________________512136____9_____________',
                '___P£___________E______52326__________________________EH8_____________',
                '__5126_________5236__________________________________5269_____________',
                '_____________________E______8___________________________9_____________',
                '_________E_£_______5316_____9___________________E__£______________Q___',
                '________5316_______________E9£__________________5326__________________',
                '_____£___________£_________£8£________________________E_9£____________',
                '____££________E_££_______EH£7£________S_______£E_____5268£_______££___',
                '0323232131231322132123123313132132131231323123121231313131132212132124',]


bossLayout = ['____________________',
                '____________________',
                'P__H________________',
                '5346________________',
                '____________________',
                '____________________',
                '____________________',
                '____________________',
                '____________________',
                '____________________',
                '____________________',
                '__________B_________',
                '02321221233213221314',]


# Measurements

tileSize = 64
scrnW = 1280
scrnH = tileSize * len(levelLayout)

# Colours
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
PURPLE = pygame.Color(200, 0, 255)
LAVA = pygame.Color(207, 16, 32)


# sound effects
pygame.mixer.init()
playerGun = pygame.mixer.Sound('sound/gun.wav')
playerJump = pygame.mixer.Sound('sound/jump.wav')
enemyGun = pygame.mixer.Sound('sound/gun1.wav')
bigEnemyGrowl = pygame.mixer.Sound('sound/growl.wav')
bigEnemyDead = pygame.mixer.Sound('sound/deathgrowl.wav')
enemyHit = pygame.mixer.Sound('sound/hit.wav')
portal = pygame.mixer.Sound('sound/portal.wav')
getItem = pygame.mixer.Sound('sound/getitem.wav')
bossMove = pygame.mixer.Sound('sound/bossmove.wav')
bossMove2 = pygame.mixer.Sound('sound/bossmove2.wav')
bossHit = pygame.mixer.Sound(('sound/bosshit.wav'))

def soundFX(volume):
    playerGun.set_volume(volume)
    playerJump.set_volume(volume)
    enemyGun.set_volume(volume)
    bigEnemyGrowl.set_volume(volume)
    bigEnemyDead.set_volume(volume)
    enemyHit.set_volume(volume)
    portal.set_volume(volume)
    getItem.set_volume(volume)
    bossMove.set_volume(volume)
    bossMove2.set_volume(volume)
    bossHit.set_volume(volume)


def music(do, track):
    if do == 'Play':
   # add music from https://freemusicarchive.org/
        pygame.mixer.music.load(f"music/bgm{track}.mp3") # Defrini - The Chonker
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)
    if do == 'Pause':
        pygame.mixer.music.pause()
    if do == 'Unpause':
        pygame.mixer.music.unpause()


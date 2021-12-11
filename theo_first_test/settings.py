# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:22:43 2021

General settings file for game

@author: theot
"""

import pygame

levelLayout = ['989888999988989998898_________________________8989898999898___________',
                '____£___D_____________________E_______E________________E_J£___________',
                '____£__536_________E£_______5316______£______________513236___________',
                '____£_________E___5326______9______5316_______£E_E______9_____________',
                '____£________516__________£_8_________________512136____9_____________',
                '___P£___________E______52326__________________________EH8_____________',
                '__5126_________5236__________________________________5269_____________',
                '_____________________E______8___________________________9_____________',
                '_________E_£_______5316_____9___________________E__£______________Q___',
                '_____Q__5316_______________E9£__________________5326__________________',
                '_____£___________£_________£8£________________________E_9£____________',
                'DJ__££________E_££_______EH£7£________S_______£E_____5268£_______££___',
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
levelLength = len(levelLayout[0])

# Colours
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
PURPLE = pygame.Color(200, 0, 255)
LAVA = pygame.Color(207, 16, 32)


def music(do, track):
    if do == 'Play':
   # add music from https://freemusicarchive.org/
        pygame.mixer.music.load(f"music/bgm{track}.mp3") # Defrini - The Chonker
        pygame.mixer.music.play(loops=-1)
    if do == 'Pause':
        pygame.mixer.music.pause()
    if do == 'Unpause':
        pygame.mixer.music.unpause()

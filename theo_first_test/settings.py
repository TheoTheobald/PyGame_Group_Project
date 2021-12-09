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
               '____£___________E_H____52326___________________________E8_____________',
               '__5126_________5236__________________________________5269_____________',
               '____________________________8___________________________9_____________',
               '_________P_£_______5316_____9___________________E__£__________________',
               '________5316_______________E9£__________________5326__________________',
               '_____£___________£_________£8£________________________E_9£____________',
               '____££________E_££________E£7£________________£E_____5268£____________',
               '0323232131231322132123123313132132131231323123121231313131132212132124',]

# levelLayout = [
#     '9_______________________________8',
#     '8__________51326_E___5126_____E_9',
#     '8_______________526_____536___518',
#     '96__516___E____________E_______59',
#     '9E_______5236____536__516_______8',
#     '826________E___£____________56__9',
#     '9____536______526______________59',
#     '8______5326P_________E5126______8',
#     '816________________536______££__8',
#     '9______E__E___H____________526__8',
#     '9____££££££££££_______2________E9',
#     '702321233212332213213213213213147',]

# Measurements

tileSize = 64
scrnW = 1200
scrnH = tileSize * len(levelLayout)
levelLength = len(levelLayout[0])

# Colours
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
PURPLE = pygame.Color(200, 0, 255)
LAVA = pygame.Color(207, 16, 32)


def timeGap(startTime, pause):
    while startTime + pause < pygame.time.get_ticks():
        pass
    return True

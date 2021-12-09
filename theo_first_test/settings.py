# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:22:43 2021

General settings file for game

@author: theot
"""

import pygame

levelLayout = ['989888999988989998898_________________________8989898999898__________8',
               '9___£___D_____________________E_______E________________E_J£__________8',
               '8___£__536_________E£_______5316______£______________513236__________8',
               '8___£_________E___5326______9______5316_______£E_E______9____________9',
               '9___£________516__________£_8_________________512136____9____________9',
               '8__P£___________E_H____52326___________________________E8____________9',
               '8_5126_________5236__________________________________5269____________8',
               '9___________________________8___________________________9____________8',
               '9__________£_______5316_____9___________________E__£____85___________9',
               '9_______5316_______________E9£__________________5326_________________8',
               '9____£___________£_________£8£________________________E_9£___________8',
               '7___££________E_££________E£7£________________£E_____5268£___________7',
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

# Colours
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
PURPLE = pygame.Color(200, 0, 255)


def timeGap(startTime, pause):
    while startTime + pause < pygame.time.get_ticks():
        pass
    return True
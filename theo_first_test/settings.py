# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:22:43 2021

General settings file for game

@author: theot
"""

import pygame

levelLayout = [
    'X_______________________________X',
    'X__________XXXXX_E___XXXX_____E_X',
    'X_______________XXX_____XXX___X_X',
    'XX_______XE____________E_______XX',
    'XE_______XXXX_________XXX_______X',
    'XXX__________________X______XX__X',
    'X___XXX_______XXX______________XX',
    'X_________P__________EXXXX______X',
    'XXX_______XX________XX_______XX_X',
    'X______E__E___H____________XXXX_X',
    'X____XXXXXXXXXX_______X________EX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]

# levelLayout = [
#     'X_______________________________X',
#     'X_______________________________X',
#     'X_______________________________X',
#     'X_______________________________X',
#     'X_______________________________X',
#     'X_____P_______________________B_X',
#     'X___XXXXX_________E_________XXXXX',
#     'X______________XXXXX____________X',
#     'X___________E___________________X',
#     'X_________XXXXX_________________X',
#     'X_____E_________E___________E___X',
#     'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',]

# Measurements

tileSize = 55
scrnW = 1200
scrnH = tileSize * len(levelLayout)

# Colours
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)

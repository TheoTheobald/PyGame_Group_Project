# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 11:56:09 2021

Enemy

@author: theot
"""

from settings import *
from character import Character


class Enemy(Character):
    className = 'enemy'

    def __init__(self, pos):
        super().__init__(pos)
        self.totalHealth = 60
        self.value = 5
        self.health = 60
        # self.hasSpace = self.checkHasSpace()
        self.getSprites(pos)
        
                            #Attempted to introduce basic enemy movement
    # def checkHasSpace(self):
    #     """This method checks if the enemy has space to move"""
    #     for platformIndex, levelPlatform in enumerate(levelLayout):
    #         for levelElementIndex, stageElement in enumerate(levelPlatform):
    #             if stageElement == "E" and self.rect.topleft == (
    #                     (levelElementIndex * tileSize), (platformIndex * tileSize)+10):
    #                 # check that the enemy has enough platform to move (at least three tiles beneath enemy)
    #                 if "_" not in levelLayout[platformIndex + 1][levelElementIndex - 1:levelElementIndex + 2]:
    #                     return True

    #     return False

    # def idleMove(self):
    #     pass
    #     if self.hasSpace():
    #         self.rect.x += 1

    # def update(self, xShift):
    #     super().update(xShift)
    #     if self.checkHasSpace():
    #         self.hasSpace = True
    #     self.idleMove()

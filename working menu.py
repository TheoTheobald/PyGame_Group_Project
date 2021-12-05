# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:32:08 2021

@author: saree
"""

import pygame, sys

clock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
WIDTH = 800
HEIGHT = 400
pygame.display.set_caption('Grandads Treasure')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
 
font = pygame.font.SysFont("Verdana", 20)

 
 
click = False
 
def menu():
    while True:
 
        surface = pygame.Surface((WIDTH,HEIGHT))
        surface.fill('black')

        main_font = pygame.font.SysFont("Verdana", 40)
        text_surface = main_font.render('Grandads Treasure', True, 'white')
        screen.blit(surface,(0,0))  
        screen.blit(text_surface,(200,10))
        
        mo_x, mo_y = pygame.mouse.get_pos()
 
        
        small_font = pygame.font.SysFont("Verdana", 20)
        instruct_surface = small_font.render('Instructions', True, 'black')
        instruct = pygame.Rect(30, 125, 200, 50)
        start_surface = small_font.render('Start', True, 'black')
        start_game = pygame.Rect(30, 200, 200, 50)
        quit_surface = small_font.render('Quit', True, 'black')
        quit_game = pygame.Rect(30, 275, 200, 50)
        if instruct.collidepoint((mo_x, mo_y)):
            if click:
                instructions()
        if start_game.collidepoint((mo_x, mo_y)):
            if click:
                game()
        if quit_game.collidepoint((mo_x, mo_y)):
            if click:
                exit_game()        
        pygame.draw.rect(screen, ('yellow'), instruct)
        screen.blit(instruct_surface,(70,140))
        pygame.draw.rect(screen, ('green'), start_game)
        screen.blit(start_surface,(100,210))
        pygame.draw.rect(screen, ('red'), quit_game)
        screen.blit(quit_surface,(100,285))
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        clock.tick(60)
        
def instructions():
    running = True
    while running:
        screen.fill(('white'))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        clock.tick(60)        
 
def game():
    running = True
    while running:
        screen.fill(('white'))
        
        #draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        clock.tick(60)
# Exit the game
def exit_game():
    running = True
    while running:
        
 
       # draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    pygame.quit()
                
        
        pygame.display.update()
        clock.tick(60)
 
menu()
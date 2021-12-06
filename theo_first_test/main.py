 # -*- coding: utf-8 -*-
"""
Spyder Editor

Level with camera that follows player - attempt 1

This is a temporary script file.
"""
import pygame, sys
from settings import *
from tiles import Tile
from level import Level

pygame.init()
scrn = pygame.display.set_mode((scrnW, scrnH))
clock = pygame.time.Clock()
level = Level(levelLayout, scrn)


pygame.display.set_caption('Grandads Treasure')
font = pygame.font.SysFont("Verdana", 20)

def menu():
    global click
    while True:
        #size of the screen
        surface = pygame.Surface((scrnW,scrnH))
        #fill screen (colour)
        surface.fill('black')
        #main title
        main_font = pygame.font.SysFont("Verdana", 40)
        text_surface = main_font.render('Grandads Treasure', True, 'white')
        scrn.blit(surface,(0,0))  
        scrn.blit(text_surface,(200,10))
        
        mo_x, mo_y = pygame.mouse.get_pos()
 
        #size of rectangle buttons and their coordinates
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
        #collidepoint function -tests if coordinates of mouse in rectangle
        if start_game.collidepoint((mo_x, mo_y)):
            if click:
                game()
        if quit_game.collidepoint((mo_x, mo_y)):
            if click:
                 pygame.quit()
                 sys.exit()
                
        pygame.draw.rect(scrn, ('yellow'), instruct)#colour of button
        scrn.blit(instruct_surface,(70,140))#positioning of text
        pygame.draw.rect(scrn, ('green'), start_game)
        scrn.blit(start_surface,(100,210))
        pygame.draw.rect(scrn, ('red'), quit_game)
        scrn.blit(quit_surface,(100,285))
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:#detects if key pressed
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #if the button is pressed
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        clock.tick(60)
# Button leads to new screen         
def instructions():
    running = True
    while running:
        scrn.fill(('white'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        clock.tick(60)        

def music():
    #add music from https://freemusicarchive.org/ 
    pygame.mixer.music.load("music/bgm1.mp3") # Defrini - The Chonker
    pygame.mixer.music.play(loops=-1)  

def game():
    
    music()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
                
            # if event.type == pygame.K_SPACE:
            #     level.bullets += level.player.shoot()
        
          
        scrn.fill('black')
        level.run()
        
        
        pygame.display.update()
        clock.tick(60)

# def game():
#     running = True
#     while running:
#         screen.fill(('white'))
        
        
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     running = False
        
#         pygame.display.update()
#         clock.tick(60)
# Exit the game
# def exit_game():
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     pygame.quit()
                
        
#         pygame.display.update()
#         clock.tick(60)
 
menu()

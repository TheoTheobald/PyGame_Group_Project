"""
Spyder Editor
Level with camera that follows player - attempt 1
This is a temporary script file.
"""

import pygame, sys
from settings import *
from level import Level


pygame.init()
scrn = pygame.display.set_mode((scrnW, scrnH))
clock = pygame.time.Clock()
level = Level(levelLayout, scrn)
bg = pygame.image.load('images/background/level_bg.png')


pygame.display.set_caption('Grandads Treasure')
font = pygame.font.SysFont("Verdana", 20)
def intro_music():
   # add music from https://freemusicarchive.org/
    pygame.mixer.music.load("music/bgm0.mp3")
    pygame.mixer.music.play(loops=-1)


def menu():
    # intro_music()
    while True:

        #size of the screen
        surface = pygame.Surface((scrnW,scrnH))
        #fill screen (colour)
        surface.fill('black')
        background = pygame.transform.scale(bg, (int(bg.get_width() * 2), int(bg.get_height() * 2)))
        surface.blit(background, (0,0))
        #main title
        main_font = pygame.font.SysFont("Calibri", 80)
        text_surface = main_font.render('Grandads Treasure', True, 'white')
        scrn.blit(surface,(0,00))
        scrn.blit(text_surface,(200,100))

        mo_x, mo_y = pygame.mouse.get_pos()


        #size of rectangle buttons and their coordinates
        small_font = pygame.font.SysFont("Verdana", 20)


        #load images
        instruct = pygame.image.load('images/buttons/button1.png')
        start = pygame.image.load('images/buttons/button2.png')
        end = pygame.image.load('images/buttons/button3.png')
        #makes drawing faster
        instruct.convert()
        start.convert()
        end.convert()

        #rescale the images
        img_width = 0.75
        img_height = 0.5
        instruct = pygame.transform.scale(instruct, (int(instruct.get_width() * img_width), int(instruct.get_height() * img_height)))
        start = pygame.transform.scale(start, (int(start.get_width() * img_width), int(start.get_height() * img_height)))
        end = pygame.transform.scale(end, (int(end.get_width() * img_width), int(end.get_height() * img_height)))


        #returns a rectangular object from the image
        rect1 = instruct.get_rect()
        rect2 = start.get_rect()
        rect3 = end.get_rect()
        #centre image rectangle to these coordinates
        FROM_LEFT = 100
        DOWN = 200
        NEXT = 100

        rect1.topleft = (FROM_LEFT,DOWN)
        rect2.topleft = (FROM_LEFT, DOWN + NEXT)
        rect3.topleft = (FROM_LEFT, DOWN + NEXT + NEXT)
        #display image
        scrn.blit(instruct, rect1)
        scrn.blit(start, rect2)
        scrn.blit(end, rect3)


        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: #if the button is pressed
                if rect1.collidepoint((mo_x, mo_y)):
                    instructions()
                #collidepoint function -tests if coordinates of mouse in rectangle
                if rect2.collidepoint((mo_x, mo_y)):
                    game()
                if rect3.collidepoint((mo_x, mo_y)):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


# Button leads to new screen
def instructions():

    running = True
    while running:
        mo_x, mo_y = pygame.mouse.get_pos()
        scrn.fill(('white'))
        back = pygame.image.load('images/buttons/button4.png')
        back.convert()
        back = pygame.transform.scale(back, (int(back.get_width() * 0.1), int(back.get_height() * 0.1)))
        rect4 = back.get_rect()
        rect4.topleft = (5,30)
        scrn.blit(back, rect4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect4.collidepoint((mo_x, mo_y)):
                    menu()
               # if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)

def music():
   # add music from https://freemusicarchive.org/
    pygame.mixer.music.load("music/bgm1.mp3") # Defrini - The Chonker
    pygame.mixer.music.play(loops=-1)

def game():
    global level
    # music()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    menu()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if level.playerkDead:
            #     level = Level(levelLayout, scrn)
            #     menu()
                
                
                


        scrn.fill('black')
        level.run()


        pygame.display.update()
        clock.tick(60)

menu()

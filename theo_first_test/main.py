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
bg = pygame.image.load('images/background/5.png')
isMuted = False


pygame.display.set_caption('KILL THE BOSS')
font = pygame.font.SysFont("Verdana", 20)
icon = pygame.image.load('images/icon/icon.png')
icon = pygame.transform.scale(icon, (32,32))
pygame.display.set_icon(icon)


def menu():
    global level
    global isMuted

    if not isMuted:
        music('Play', 0)
    while True:
        surface = pygame.Surface((scrnW,scrnH))

        #fill screen (colour)
        surface.fill('black')
        background = pygame.transform.scale(bg, (int(bg.get_width() * 2), int(bg.get_height() * 2)))
        surface.blit(background, (0,0))
        #main title
        main_font = pygame.font.Font('fonts/Barcade.otf', 100)
        text_surface = main_font.render('(KILL THE BOSS)', True, 'white')
        scrn.blit(surface,(0,00))
        scrn.blit(text_surface,(260, 80))

        mo_x, mo_y = pygame.mouse.get_pos()


        #size of rectangle buttons and their coordinates
        small_font = pygame.font.SysFont("Verdana", 20)


        #load images
        instruct = pygame.image.load('images/buttons/button1.png')
        start = pygame.image.load('images/buttons/button2.png')
        end = pygame.image.load('images/buttons/button3.png')
        audio = pygame.image.load('images/buttons/pause.png')
        #makes drawing faster
        instruct.convert()
        start.convert()
        end.convert()
        audio.convert()

        #rescale the images
        img_width = 0.75
        img_height = 0.5
        instruct = pygame.transform.scale(instruct, (int(instruct.get_width() * img_width), int(instruct.get_height() * img_height)))
        start = pygame.transform.scale(start, (int(start.get_width() * img_width), int(start.get_height() * img_height)))
        end = pygame.transform.scale(end, (int(end.get_width() * img_width), int(end.get_height() * img_height)))
        audio = pygame.transform.scale(audio, (int(audio.get_width() * 0.1), int(audio.get_height() * 0.1)))

        #returns a rectangular object from the image
        rect1 = instruct.get_rect()
        rect2 = start.get_rect()
        rect3 = end.get_rect()
        rect5 = audio.get_rect()
        #centre image rectangle to these coordinates
        DOWN = 250
        NEXT = 50

        rect1.center = (scrnW // 2, DOWN + NEXT)
        rect2.center = (scrnW // 2, DOWN + NEXT * 3)
        rect3.center = (scrnW // 2, DOWN + NEXT * 5)
        rect5.topleft = (50, 728)
        #display image
        scrn.blit(instruct, rect1)
        scrn.blit(start, rect2)
        scrn.blit(end, rect3)
        scrn.blit(audio, rect5)



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
                if rect5.collidepoint((mo_x, mo_y)):
                    #boolean

                    if not isMuted:
                        music('Pause', 0)
                        isMuted = True
                    elif isMuted:
                        music('Unpause', 0)
                        isMuted = False


        pygame.display.update()
        clock.tick(60)


# Button leads to new screen
def instructions():


    while True:
        mo_x, mo_y = pygame.mouse.get_pos()
       # scrn.fill(('white'))


        bg = pygame.image.load('images/background/inst_bg.png')
        bg.convert()
        bg = pygame.transform.scale(bg, (int(bg.get_width() * 1.35), int(bg.get_height() * 1.55)))
        rect6 = bg.get_rect()
        rect6.topleft = (0,50)
        scrn.blit(bg, rect6)

        # stating points value of each enemy


        back = pygame.image.load('images/buttons/button4.png')
        back.convert()
        back = pygame.transform.scale(back, (int(back.get_width() * 0.1), int(back.get_height() * 0.1)))
        rect4 = back.get_rect()
        rect4.topleft = (5,60)
        scrn.blit(back, rect4)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect4.collidepoint((mo_x, mo_y)):
                    menu()
                    running = False

        pygame.display.update()
        clock.tick(60)

def game():
    global level
    global isMuted

    if not isMuted:
        music('Play', 1)
        soundFX(1)
    elif isMuted:
        music('Pause', 1)
        soundFX(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # If escape is pressed, return to menu
                if event.key == pygame.K_ESCAPE:
                    menu()
                if event.key == pygame.K_RETURN and (level.player.sprite.dead == True or level.gameComplete == True):
                    level = Level(levelLayout, scrn) # If game is over, return to menu when enter is pressed
                    menu()
            if event.type == pygame.QUIT: # If game is closed, close
                pygame.quit()
                sys.exit()
            if level.teleportPlayer == True: # When player touches portal and has killed red dude, rebuilt level to boss room
                player = level.player.sprite
                level = Level(bossLayout, scrn)
                player.rect = level.player.sprite.rect # Player assigned to temp variable so that data is not lost
                level.player.sprite = player # Everything about old player barring position is retained
                music('Play', 2)


        scrn.fill('black')
        level.run()


        pygame.display.update()
        clock.tick(60)

menu()

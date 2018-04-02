
# platform_game.py
# By: {group members names}
# Date created: March 1st, 2018
# This program is a simple game that was made by SMC programming club members.
# Game is meant to be a simple platform game with eniemies, platforms, lives,
# a timer, and an end
# Built with the pygame library.

#Iimporting libraries that are needed to run the game

import pygame
import sys

def menu():
   #import pygame, sys

def gameFunction():
    #print("Text from gameFunction")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def buttonHover(mouse, screen, myFont):
    if int(mouse[0]) >= 350 and int(mouse[0]) <= 500 and int(mouse[1]) >= 200 and int(mouse[1]) <= 350:
        #print("mouse inside button")
        button = pygame.Rect(350,200,150,150)
        pygame.draw.rect(screen, [0,255,0], button)

        buttonText = myFont.render('Start Game', False, (0,0,0))
        screen.blit(buttonText, (355, 200))
        pygame.display.flip()
    else:
        #print("mouse outside button")
        button = pygame.Rect(350,200,150,150)
        pygame.draw.rect(screen, [255,0,0], button)

        buttonText = myFont.render('Start Game', False, (0,0,0))
        screen.blit(buttonText, (355, 200))
        pygame.display.flip()
        
def menuMain():
    pygame.init()
    pygame.font.init()

    pygame.display.set_caption('Platformer_Game')

    width = 800
    height = 600

    screen = pygame.display.set_mode([width,height])
    blue  = [0  ,255,255]
    white = [255,255,255]
    screen.fill(blue)

    myFont = pygame.font.SysFont('Times', 30)
    textSurface = myFont.render('Platformer_Game', False, (0, 0, 0))
    screen.blit(textSurface, (300, 100))
    
    button = pygame.Rect(350,200,150,150)
    pygame.draw.rect(screen, [255,0,0], button)

    buttonText = myFont.render('Start Game', False, (0,0,0))
    screen.blit(buttonText, (355, 200))

    pygame.display.flip()

    gameControl = True

    while gameControl:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        buttonHover(mouse, screen, myFont)

        if int(mouse[0]) >= 350 and int(mouse[0]) <= 500 and int(mouse[1]) >= 200 and int(mouse[1]) <= 350:
            if click[0] == 1:
                screen.fill(white)
                pygame.display.flip()
                gameFunction()
                gameControl = False
                
    menuMain()
    
# Importanting classes from seperate files in order to be organized
import lib.menu as menu

# declaring constants
WIDTH = 700
HEIGHT = 500

# Game needs Pyhthon 3 and higher in order to be ran without errors
if sys.version_info[0] < 3:
    raise "Ran with Python 2. Needed Python 3."


# initalizing pygame
pygame.init()

# defining the window
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Platform Game")

# setting up clock for refresh rate
clock = pygame.time.Clock()

# varible used to control the game loop
done = False

# --- GAME LOOP ---
while not done:
    # setting up control for the game to quit when ordered to
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # *************************
    # ** GAME CODE GOES HERE **
    # *************************

    

    # *************************
    # **    END GAME CODE    **
    # *************************

    # setting frame rate at 60
    clock.tick(60)

# shutting down the game
pygame.quit()


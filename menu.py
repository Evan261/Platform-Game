import pygame, sys

def menu():
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

menu()

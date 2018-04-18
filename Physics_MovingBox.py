import pygame, sys, time

def main():

        pygame.font.init()

        pygame.display.set_caption('Platformer_Game')

        width = 800
        height = 600

        screen = pygame.display.set_mode([width,height])
        blue  = [0  ,255,255]
        white = [255,255,255]

        button_X1 = 0
        button_Y1 = 0

        Platform_X1 = 100
        Platform_Y1 = 400
        
        gameControl = True

        clock = pygame.time.Clock()

        keys = pygame.key.get_pressed()

        foo = 0
        bar = 5

        while gameControl:

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if ((event.key == pygame.K_UP) and (button_Y1 == 500)):
                        foo = 10
                    if event.key == pygame.K_RIGHT:
                        if(button_X1 < 700):
                            button_X1 += 50
                    if event.key == pygame.K_LEFT:
                        if(button_X1 > 0):
                            button_X1 -= 50

            
            if(foo > bar):
                button_Y1 -= 50
                foo -= 1
                if(button_Y1 == (Platform_Y1 - 100)):
                    foo == 0

                          
        
            test = True

            #if(button_Y1 < 90 and button_Y1 > 50 and button_X1 < 250 and button_X1 > 100):
            #    test = False

              
            if(button_Y1 < 500):
                button_Y1+=10
                #button_Y2+=1
            
            screen.fill(white)
            
            button = pygame.Rect(button_X1,button_Y1,100,100)
            pygame.draw.rect(screen, [255,0,0], button)

            platform = pygame.Rect(Platform_X1,Platform_Y1,100,100)
            pygame.draw.rect(screen, [0,255,0], platform)

            pygame.display.flip()
            clock.tick(60)

            

main()

            

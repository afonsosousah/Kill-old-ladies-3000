import pygame
import pygame.gfxdraw
import sys
from multiplayer_game import multiplayer_racing
import interface
import main

# Creating a function that creates the GUI
def multiplayer_car_selector():
    # initiating pygames
    pygame.init()
    
    # creating the screen 720x720 pixels
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    
    # setting the window title
    pygame.display.set_caption("Turbo Racing 3000")
    
    # creatinbg some colors (RGB scale)
    white = (255, 255, 255)
    yellow = (253, 210, 48)
    red = (255, 0, 0)
    color_light = (170, 170, 170)

    
    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()
    
    # creating title text label
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 50)
    title_text = comicsansfont.render('Turbo Racing 3000', True, yellow)
    
    # creating buttons text labels
    font = pygame.font.Font('fonts/MASQUE__.ttf', 28)
    play_text = font.render('Play', True, white)
    back_text = font.render('Back', True, white)

    # creating player1 and player2 text
    font = pygame.font.Font('fonts/MASQUE__.ttf', 28)
    player1_text = font.render('Player One', True, white)
    player1_rect = player1_text.get_rect(center = (200,170))
    player2_text = font.render('Player Two', True, white)
    player2_rect = player1_text.get_rect(center = (520,170))
    
    # Allowing the user to close the window...
    carryOn = True
    clock=pygame.time.Clock()

    # store the selected car
    main.selected_car = 1
    main.selected_car2 = 2

    # Create the infinite scrolling background for the menu
    MAP = pygame.image.load("assets/infinite_level.png").convert_alpha()
    MAP = pygame.transform.scale_by(MAP, 0.9)
    mapY0 = -200
    mapY1 = -1280
    
    # interface loop
    while carryOn:
        # getting the input of the user
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press the back button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                print(mouse)
                if 150 <= mouse[0] <= 300 and 560 <= mouse[1] <= 620:
                    interface.interface()
            # pressing the play button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 400 <= mouse[0] <= 550 and 560 <= mouse[1] <= 620:
                    multiplayer_racing()
            # pressing the next car button1
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 276 <= mouse[0] <= 341 and 250 <= mouse[1] <= 330:
                    if main.selected_car + 1 != main.selected_car2: # Don't let both players choose the same car
                        if main.selected_car + 1 <= 6:
                            main.selected_car += 1
                        else:
                            main.selected_car = 1
                    else: # If the car would be the same, skip to the next one
                        if main.selected_car + 2 <= 6:
                            main.selected_car += 2
                        else:
                            main.selected_car = 1
            # pressing the previous car button1
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 57 <= mouse[0] <= 122 and 250 <= mouse[1] <= 330:
                    if main.selected_car - 1 != main.selected_car2: # Don't let both players choose the same car
                        if main.selected_car - 1 >= 1:
                            main.selected_car -= 1
                        else:
                            main.selected_car = 6
                    else: # If the car would be the same, skip to the next one
                        if main.selected_car - 2 >= 1:
                            main.selected_car -= 2
                        else:
                            main.selected_car = 6
            # pressing the next car button2
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 591 <= mouse[0] <= 656 and 250 <= mouse[1] <= 330:
                    if main.selected_car2 + 1 != main.selected_car: # Don't let both players choose the same car
                        if main.selected_car2 + 1 <= 6:
                            main.selected_car2 += 1
                        else:
                            main.selected_car2 = 1
                    else: # If the car would be the same, skip to the next one
                        if main.selected_car2 + 2 <= 6:
                            main.selected_car2 += 2
                        else:
                            main.selected_car2 = 1
            # pressing the previous car button2
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 386 <= mouse[0] <= 451 and 250 <= mouse[1] <= 330:
                    if main.selected_car2 - 1 != main.selected_car: # Don't let both players choose the same car
                        if main.selected_car2 - 1 >= 1:
                            main.selected_car2 -= 1
                        else:
                            main.selected_car2 = 6
                    else: # If the car would be the same, skip to the next one
                        if main.selected_car2 - 2 >= 1:
                            main.selected_car2 -= 2
                        else:
                            main.selected_car2 = 6
            
        # Infinite scrolling map as background
        screen.blit(MAP, [0, mapY0, 720, 1080])
        screen.blit(MAP, [0, mapY1, 720, 1080])
        if mapY0 > -300:
            mapY1 = mapY0 - 1080
        if mapY1 > -300:
            mapY0 = mapY1 - 1080
        # move the map 
        mapY0 += 1
        mapY1 += 1
        
        # Transparent black mid layer
        transparent_black = pygame.image.load('assets/empty.png')
        transparent_black = pygame.transform.scale(transparent_black, (720, 720))
        screen.blit(transparent_black, (0,0))
    
        
        # print the buttons text and the box(color changing)
        
        # play text
        mouse = pygame.mouse.get_pos()
        # when the mouse is on the box it changes color
        if 400 <= mouse[0] <= 550 and 560 <= mouse[1] <= 620:
            interface.drawRhomboid(screen, yellow, white, 400, 560, 150, 60, 30, 5)
        else:
            interface.drawRhomboid(screen, yellow, yellow, 400, 560, 150, 60, 30, 5)
        screen.blit(play_text, (400 + 12.5 + (150 - play_text.get_width())/2, 560 + 12.5)) # +12.5 in the width and height because of the rhomboid offset and border
        
        # quit text
        if 150 <= mouse[0] <= 300 and 560 <= mouse[1] <= 620:
            interface.drawRhomboid(screen, red, white, 150, 560, 150, 60, 30, 5)
        else:
            interface.drawRhomboid(screen, red, red, 150, 560, 150, 60, 30, 5)
        screen.blit(back_text, (150 + 12.5 + (150 - back_text.get_width())/2, 560 + 12.5)) 
        
        # draw the car
        car_image1 = pygame.image.load(f'assets/car{main.selected_car}.png')
        car_image1 = pygame.transform.scale(car_image1, (car_image1.get_width()*2, car_image1.get_height()*2))  # scale up the image
        screen.blit(car_image1, (200 - car_image1.get_width()/2, 200))

        # draw the other car
        car_image2 = pygame.image.load(f'assets/car{main.selected_car2}.png')
        car_image2 = pygame.transform.scale(car_image2, (car_image2.get_width()*2, car_image2.get_height()*2))  # scale up the image
        screen.blit(car_image2, (525 - car_image2.get_width()/2, 200))
        
        # draw the change selected car buttons
        pygame.draw.polygon(screen, color_light, ((122,250),(122,330),(57,290)))
        pygame.draw.polygon(screen, color_light, ((276,250),(276,330),(341,290)))

        # draw the other change selected car buttons
        pygame.draw.polygon(screen, color_light, ((451,250), (451,330), (386,290)))
        pygame.draw.polygon(screen, color_light, ((591,250), (591,330), (656,290)))

        # player1 and player2 text
        screen.blit(player1_text, player1_rect)
        screen.blit(player2_text, player2_rect)
        
        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
        pygame.display.update()



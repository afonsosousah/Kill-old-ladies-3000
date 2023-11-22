import pygame
import pygame.gfxdraw
import sys
from game import car_racing
import interface
import main

# Creating a function that creates the GUI
def car_selector():
    # initiating pygames
    pygame.init()
    
    # creating the screen 720x720 pixels
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    
    # setting the window title
    pygame.display.set_caption("Turbo Racing 3000")
    
    # creatinbg some colors (RGB scale)
    white = (255, 255, 255)
    yellow = (253, 199, 79)
    red = (255, 0, 0)
    green = (110, 218, 44)
    blue = (0, 0, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    black = (0, 0, 0)
    
    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()
    
    # creating title text label
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 50)
    title_text = comicsansfont.render('Turbo Racing 3000', True, yellow)
    
    # creating buttons text labels
    corbelfont = pygame.font.SysFont('Corbel', 40, bold=True, italic=True)
    play_text = corbelfont.render('Play', True, white)
    back_text = corbelfont.render('Back', True, white)
    
    # Allowing the user to close the window...
    carryOn = True
    clock=pygame.time.Clock()

    # store the selected car
    main.selected_car = 1
    
    # interface loop
    while carryOn:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press the back button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 150 <= mouse[0] <= 300 and 560 <= mouse[1] <= 620:
                    interface.interface()
            # pressing the play button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 400 <= mouse[0] <= 550 and 560 <= mouse[1] <= 620:
                    car_racing()
            # pressing the next car button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 465 <= mouse[0] <= 530 and 250 <= mouse[1] <= 330:
                    if main.selected_car + 1 <= 6:
                        main.selected_car += 1
                    else:
                        main.selected_car = 1
            # pressing the previous car button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 190 <= mouse[0] <= 250 and 250 <= mouse[1] <= 330:
                    if main.selected_car - 1 >= 1:
                        main.selected_car -= 1
                    else:
                        main.selected_car = 6
            
            
        # setting the background color as black
        screen.fill(black)
        
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
        car_image = pygame.image.load(f'assets/car{main.selected_car}.png')
        car_image = pygame.transform.scale(car_image, (car_image.get_width()*3, car_image.get_height()*3))  # scale up the image
        screen.blit(car_image, (360 - car_image.get_width()/2, 150))
        
        # draw the change selected car buttons
        pygame.draw.polygon(screen, color_light, ((465,250),(465,330),(530,290)))
        pygame.draw.polygon(screen, color_light, ((250,250),(250,330),(190,290)))
        
        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
        pygame.display.update()
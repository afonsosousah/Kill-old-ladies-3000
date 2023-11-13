import pygame
import sys
from game import car_racing


# Creating a function that creates the GUI
def interface():
    # initiating pygames
    pygame.init()
    # creating the screen 720x720 pixels
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    # creatinbg some colors (RGB scale)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    black = (0, 0, 0)
    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()
    # creating some textlabels
    corbelfont = pygame.font.SysFont('Corbel', 50)
    game1_text = corbelfont.render('Car Racing', True, blue)
    game2_text = corbelfont.render('game2', True, blue)
    game3_text = corbelfont.render('game3', True, blue)
    credits_text = corbelfont.render('credits', True, blue)
    quit_text = corbelfont.render('   quit', True, blue)
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 50)
    title_text = comicsansfont.render('Computation III - Project', True, yellow)
    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                print(width)
                print(height)
                if 450 <= mouse[0] <= 590 and 600<= mouse[1] <= 660:
                    pygame.quit()
            # press the credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 480 <= mouse[1] <= 540:
                    credits_()
            # pressing the pong button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 90 <= mouse[0] <= 230 and 240 <= mouse[1] <= 300:
                    car_racing()
        # setting the background color as black
        screen.fill(black)
        # print the buttons text and the box(color changing)
        # game 1 text
        mouse = pygame.mouse.get_pos()
        # when the mouse is on the box it changes color
        if 90 <= mouse[0] <= 230 and 240 <= mouse[1] <= 300:
            pygame.draw.rect(screen, green, [90, 240, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [90, 240, 140, 60])
        screen.blit(game1_text, (90, 240))
        # SAME FOR ALL THE OTHER BUTTONS
        # game 2 text
        if 450 <= mouse[0] <= 450 + 140 and 240 <= mouse[1] <= 240 + 60:
            pygame.draw.rect(screen, green, [450, 240, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [450, 240, 140, 60])
        screen.blit(game2_text, (450, 240))
        # game 3 text
        if 90 <= mouse[0] <= 90 + 140 and 4 * 120 <= mouse[1] <= 4 * 120 + 60:
            pygame.draw.rect(screen, green, [90, 4 * 120, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [90, 4 * 120, 140, 60])
        screen.blit(game3_text, (90, 4 * 120))
        # credits text
        if 450 <= mouse[0] <= 450 + 140 and 4 * 120 <= mouse[1] <= 4 * 120 + 60:
            pygame.draw.rect(screen, yellow, [450, 4 * 120, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [450, 4 * 120, 140, 60])
        screen.blit(credits_text, (450, 4 * 120))
        # quit text
        if 450 <= mouse[0] <= 450 + 140 and 5 * 120 <= mouse[1] <= 5 * 120 + 60:
            pygame.draw.rect(screen, red, [450, 5 * 120, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [450, 5 * 120, 140, 60])
        screen.blit(quit_text, (450, 5 * 120))
        # TITLE TEXT
        # pygame.draw.rect(screen, color_dark, [52, 0, 612, 100])
        screen.blit(title_text, (55, 0))
        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
        pygame.display.update()


def credits_():
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    height = screen.get_height()
    corbelfont = pygame.font.SysFont('Corbel', 50)
    back_text = corbelfont.render('   back', True, blue)
    comicsansfont = pygame.font.SysFont('Comic Sans MS', 25)
    line1_text = comicsansfont.render('Davide Farinati, dfarinati@novaims.unl.pt', True, yellow)
    line2_text = comicsansfont.render('Joao Fonseca, jfonseca@novaims.unl.pt', True, yellow)
    line3_text = comicsansfont.render('Liah Rosenfeld, lrosenfeld@novaims.unl.pt', True, yellow)

    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 450 + 140 and 5 * 120 <= mouse[
                    1] <= 5 * 120 + 60:
                    interface()
        screen.fill((0, 0, 0))
        # credits text
        screen.blit(line1_text, (0, 0))
        screen.blit(line2_text, (0, 25))
        screen.blit(line3_text, (0, 50))
        # back text
        if 450 <= mouse[0] <= 450 + 140 and 5 * 120 <= mouse[1] <= 5 * 120 + 60:
            pygame.draw.rect(screen, red, [450, 5 * 120, 140, 60])
        else:
            pygame.draw.rect(screen, color_dark, [450, 5 * 120, 140, 60])
        screen.blit(back_text, (450, 5 * 120))

        pygame.display.update()
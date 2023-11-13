import pygame
import pygame.gfxdraw
import sys
from game import car_racing


# Creating a function that creates the GUI
def interface():
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
    game1_text = corbelfont.render('Singleplayer', True, white)
    game2_text = corbelfont.render('Multiplayer', True, white)
    game3_text = corbelfont.render('Infinite Mode', True, white)
    credits_text = corbelfont.render('Credits', True, white)
    quit_text = corbelfont.render('Quit', True, white)
    
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
                if 210 <= mouse[0] <= 210 + 300 and 560 <= mouse[1] <= 560 + 60:
                    pygame.quit()
            # press the credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 210 <= mouse[0] <= 210 + 300 and 480 <= mouse[1] <= 480 + 60:
                    credits_()
            # pressing the singleplayer button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 210 <= mouse[0] <= 510 and 240 <= mouse[1] <= 300:
                    car_racing()
        # setting the background color as black
        screen.fill(black)
        
        # print the buttons text and the box(color changing)
        
        # game 1 text
        mouse = pygame.mouse.get_pos()
        # when the mouse is on the box it changes color
        if 210 <= mouse[0] <= 510 and 240 <= mouse[1] <= 300:
            drawRhomboid(screen, yellow, yellow, 195, 240, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, yellow, white, 195, 240, 300, 60, 30, 5)
        screen.blit(game1_text, (210 + (300 - game1_text.get_width())/2, 240 + 10))
        
        # SAME FOR ALL THE OTHER BUTTONS
        # game 2 text
        if 210 <= mouse[0] <= 210 + 300 and 320 <= mouse[1] <= 320 + 60:
            drawRhomboid(screen, yellow, yellow, 195, 320, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, yellow, white, 195, 320, 300, 60, 30, 5)
        screen.blit(game2_text, (210 + (300 - game2_text.get_width())/2, 320 + 10))
        
        # game 3 text
        if 210 <= mouse[0] <= 210 + 300 and 400 <= mouse[1] <= 400 + 60:
            drawRhomboid(screen, yellow, yellow, 195, 400, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, yellow, white, 195, 400, 300, 60, 30, 5)
        screen.blit(game3_text, (210 + (300 - game3_text.get_width())/2, 400 + 10))
        
        # credits text
        if 210 <= mouse[0] <= 210 + 300 and 480 <= mouse[1] <= 480 + 60:
            drawRhomboid(screen, green, green, 195, 480, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, green, white, 195, 480, 300, 60, 30, 5)
        screen.blit(credits_text, (210 + (300 - credits_text.get_width())/2, 480 + 10))
        
        # quit text
        if 210 <= mouse[0] <= 210 + 300 and 560 <= mouse[1] <= 560 + 60:
            drawRhomboid(screen, red, red, 195, 560, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, red, white, 195, 560, 300, 60, 30, 5)
        screen.blit(quit_text, (210 + (300 - quit_text.get_width())/2, 560 + 10))
        
        # TITLE TEXT
        # pygame.draw.rect(screen, color_dark, [52, 0, 612, 100])
        screen.blit(title_text, ((720 - title_text.get_width())/2, 50))
        
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



def drawRhomboid(surface, color, outline_color, x, y, width, height, offset, thickness=0):
    points = [
        (x + offset, y), 
        (x + width + offset, y), 
        (x + width, y + height), 
        (x, y + height)]
    inner_points = [
        (x + offset + thickness, y + thickness), 
        (x + width + offset - 2*thickness, y + thickness), 
        (x + width - thickness, y + height - thickness), 
        (x + 2*thickness, y + height - thickness)]
    pygame.gfxdraw.filled_polygon(surface, points, color)
    pygame.draw.polygon(surface, outline_color, points, thickness)
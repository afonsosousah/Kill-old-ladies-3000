import pygame
import pygame.gfxdraw
import sys
from car_selector import car_selector
from multiplayer_car_selector import multiplayer_car_selector


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
    #comicsansfont = pygame.font.SysFont('Comic Sans MS', 50)
    #title_text = comicsansfont.render('Turbo Racing 3000', True, yellow)
    
    # creating buttons text labels
    corbelfont = pygame.font.SysFont('Corbel', 40, bold=True, italic=True)
    game1_text = corbelfont.render('Singleplayer', True, white)
    game2_text = corbelfont.render('Multiplayer', True, white)
    game3_text = corbelfont.render('How to Play', True, white)
    credits_text = corbelfont.render('Credits', True, white)
    quit_text = corbelfont.render('Quit', True, white)
    
    # Create the infinite scrolling background for the menu
    MAP = pygame.image.load("assets/infinite_level.png").convert_alpha()
    MAP = pygame.transform.scale_by(MAP, 0.9)
    mapY0 = -200
    mapY1 = -1280
    
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
                    car_selector()
            # pressing the multiplayer button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 210 <= mouse[0] <= 210 + 300 and 320 <= mouse[1] <= 320 + 60:
                    multiplayer_car_selector()
                    pass
        
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
        
        # game 1 text
        mouse = pygame.mouse.get_pos()
        # when the mouse is on the box it changes color
        if 210 <= mouse[0] <= 510 and 240 <= mouse[1] <= 300:
            drawRhomboid(screen, yellow, white, 195, 240, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, yellow, yellow, 195, 240, 300, 60, 30, 5)
        screen.blit(game1_text, (210 + (300 - game1_text.get_width())/2, 240 + 10))
        
        # SAME FOR ALL THE OTHER BUTTONS
        # game 2 text
        if 210 <= mouse[0] <= 210 + 300 and 320 <= mouse[1] <= 320 + 60:
            drawRhomboid(screen, yellow, white, 195, 320, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, yellow, yellow, 195, 320, 300, 60, 30, 5)
        screen.blit(game2_text, (210 + (300 - game2_text.get_width())/2, 320 + 10))
        
        # game 3 text
        if 210 <= mouse[0] <= 210 + 300 and 400 <= mouse[1] <= 400 + 60:
            drawRhomboid(screen, yellow, white, 195, 400, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, yellow, yellow, 195, 400, 300, 60, 30, 5)
        screen.blit(game3_text, (210 + (300 - game3_text.get_width())/2, 400 + 10))
        
        # credits text
        if 210 <= mouse[0] <= 210 + 300 and 480 <= mouse[1] <= 480 + 60:
            drawRhomboid(screen, green, white, 195, 480, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, green, green, 195, 480, 300, 60, 30, 5)
        screen.blit(credits_text, (210 + (300 - credits_text.get_width())/2, 480 + 10))
        
        # quit text
        if 210 <= mouse[0] <= 210 + 300 and 560 <= mouse[1] <= 560 + 60:
            drawRhomboid(screen, red, white, 195, 560, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, red, red, 195, 560, 300, 60, 30, 5)
        screen.blit(quit_text, (210 + (300 - quit_text.get_width())/2, 560 + 10))
        
        # TITLE TEXT
        # pygame.draw.rect(screen, color_dark, [52, 0, 612, 100])
        #screen.blit(title_text, ((720 - title_text.get_width())/2, 50))
        
        # Display word art
        title_wordart = pygame.image.load('assets/wordart.png')
        title_wordart = pygame.transform.scale_by(title_wordart, 0.16)
        screen.blit(title_wordart, (720/2 - title_wordart.get_width()/2, -70))
        
        # PYGAME BUILT IN FUCTION that updates the screen at every oteration of the loop
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


def credits_():
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    
    # creating some important colors
    white = (255, 255, 255)
    red = (255, 0, 0)

    width = screen.get_width()
    height = screen.get_height()
    #credits_background = pygame.image.load("assets/credits.png")
    

    # creating buttons text label
    corbelfont = pygame.font.SysFont('Corbel', 40, bold=True, italic=True)
    back_text = corbelfont.render('Back', True, white)

    # comicsansfont = pygame.font.SysFont('Comic Sans MS', 25)
    # line1_text = comicsansfont.render('Afonso Hermenegildo, 20221958', True, yellow)
    # line2_text = comicsansfont.render('Diogo Oliveira, 20221928', True, yellow)
    # line3_text = comicsansfont.render('Tomás Rodrigues, 20221956', True, yellow)
    
    gif_frame = 0

    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press the back button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 75 <= mouse[0] <= 225 and 620 <= mouse[1] <= 680:
                    interface()
        
        # Show the frames of the credits gif
        if gif_frame != 47:
            screen.blit(pygame.image.load(f'assets/credits_gif_frames/frame_{gif_frame}.png'), (0,0))
            gif_frame += 1
        else:
            screen.blit(pygame.image.load(f'assets/credits_gif_frames/frame_{gif_frame}.png'), (0,0))
            gif_frame = 0
            
        pygame.time.delay(30)
                                    
        #screen.blit(pygame.image.load('assets/credits.png'), [0, 0, width, height])

        # credits text
        # screen.blit(line1_text, (0, 0))
        # screen.blit(line2_text, (0, 25))
        # screen.blit(line3_text, (0, 50))
        
        # back text
        if 75 <= mouse[0] <= 225 and 620 <= mouse[1] <= 680:
            drawRhomboid(screen, red, white, 75, 620, 150, 60, 30, 5)
        else:
            drawRhomboid(screen, red, red, 75, 620, 150, 60, 30, 5)
        screen.blit(back_text, (75 + 12.5 + (150 - back_text.get_width())/2, 620 + 12.5))

        pygame.display.update()

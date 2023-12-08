import pygame
import pygame.gfxdraw
from car_selector import car_selector
from multiplayer_car_selector import multiplayer_car_selector


def interface():
    """Main Game Interface

    This function provides the main game interface for the Turbo Racing 3000 game.
    It manages the game menu, including buttons for singleplayer, multiplayer, how to play, credits, and quit.
    It also handles user input and transitions between different game modes based on user selection.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    
    # initiating pygames
    pygame.init()
    
    # creating the screen 720x720 pixels
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    
    # setting the window title
    pygame.display.set_caption("Turbo Racing 3000")
    
    # setting the icon
    pygame.display.set_icon(pygame.image.load("assets/icon.png"))
    
    # creating some colors (RGB scale)
    white = (255, 255, 255)
    yellow = (255, 210, 48)
    red = (255, 0, 0)
    green = (135, 203, 40)

    
    # saving the screen sizes
    width = screen.get_width()
    height = screen.get_height()
    
    # creating buttons text labels
    font = pygame.font.Font('fonts/MASQUE__.ttf', 28)
    singleplayer_text = font.render('Singleplayer', True, white)
    multiplayer_text = font.render('Multiplayer', True, white)
    howtoplay_text = font.render('How to Play', True, white)
    credits_text = font.render('Credits', True, white)
    quit_text = font.render('Quit', True, white)
    
    # Create the infinite scrolling background for the menu
    MAP = pygame.image.load("assets/infinite_level.png").convert_alpha()
    MAP = pygame.transform.scale_by(MAP, 0.9)
    mapY0 = -200
    mapY1 = -1280
    
    # Play game soundtrack
    pygame.mixer.music.load('assets/game_soundtrack.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.7)
    
    # interface loop
    while True:
        # getting the input of the user
        for ev in pygame.event.get():
            # press on exit button
            if ev.type == pygame.QUIT:
                pygame.quit()
            # press on quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 210 <= mouse[0] <= 210 + 300 and 560 <= mouse[1] <= 560 + 60:
                    pygame.quit()
            # press the credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 210 <= mouse[0] <= 210 + 300 and 480 <= mouse[1] <= 480 + 60:
                    credits_()
            # press the how to play button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 210 <= mouse[0] <= 210 + 300 and 400 <= mouse[1] <= 400 + 60:
                    how_to_play()
            # pressing the singleplayer button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 210 <= mouse[0] <= 510 and 240 <= mouse[1] <= 240 + 60:
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
        
        
        # draw the buttons text and the box(color changing)
        
        # singleplayer text
        mouse = pygame.mouse.get_pos()
        # when the mouse is on the box it changes color
        if 210 <= mouse[0] <= 510 and 240 <= mouse[1] <= 300:
            drawRhomboid(screen, yellow, white, 195, 240, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, yellow, yellow, 195, 240, 300, 60, 30, 5)
        screen.blit(singleplayer_text, (210 + (300 - singleplayer_text.get_width())/2, 240 + 10))
        
        # SAME FOR ALL THE OTHER BUTTONS
        # multiplayer text
        if 210 <= mouse[0] <= 210 + 300 and 320 <= mouse[1] <= 320 + 60:
            drawRhomboid(screen, yellow, white, 195, 320, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, yellow, yellow, 195, 320, 300, 60, 30, 5)
        screen.blit(multiplayer_text, (210 + (300 - multiplayer_text.get_width())/2, 320 + 10))
        
        # how to play text
        if 210 <= mouse[0] <= 210 + 300 and 400 <= mouse[1] <= 400 + 60:
            drawRhomboid(screen, yellow, white, 195, 400, 300, 60, 30, 5)
        else:
            drawRhomboid(screen, yellow, yellow, 195, 400, 300, 60, 30, 5)
        screen.blit(howtoplay_text, (210 + (300 - howtoplay_text.get_width())/2, 400 + 10))
        
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


# Function that draws the rhomboids used as the buttons
def drawRhomboid(surface, color, outline_color, x, y, width, height, offset, thickness=0):
    """Draw Rhomboid Button

    This function draws a rhomboid-shaped button with optional border using Pygame's graphics drawing functions.

    Parameters
    ----------
    surface: pygame.Surface
        Target surface to draw the rhomboid onto.
    color: tuple(int, int, int)
        Color of the filled rhomboid.
    outline_color: tuple(int, int, int)
        Color of the optional border.
    x: int
        Horizontal position of the top-left corner of the rhomboid.
    y: int
        Vertical position of the top-left corner of the rhomboid.
    width: int
        Width of the rhomboid.
    height: int
        Height of the rhomboid.
    offset: int
        Offset from the top-left corner of the rhomboid for the filled rhomboid.
    thickness: int, optional
        Thickness of the border, default is 0.

    Returns
    -------
    None

    """
    
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
    """Show Credits Screen

    This function displays the credits screen of the Turbo Racing 3000 game.
    It loads and displays the credits GIF animation, plays the credits soundtrack, and handles user input for the back button.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """


    res = (720, 720)
    screen = pygame.display.set_mode(res)
    
    # creating some important colors
    white = (255, 255, 255)
    red = (255, 0, 0)

    width = screen.get_width()
    height = screen.get_height()

    # creating buttons text label
    font = pygame.font.Font('fonts/MASQUE__.ttf', 28)
    back_text = font.render('Back', True, white)

    # Play credits soundtrack
    pygame.mixer.music.load('assets/credits_soundtrack.mp3')
    pygame.mixer.music.play(-1)
    
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
                    pygame.mixer.music.stop()
                    interface()
        
        # Show the frames of the credits gif
        if gif_frame != 47:
            screen.blit(pygame.image.load(f'assets/credits_gif_frames/frame_{gif_frame}.png'), (0,0))
            gif_frame += 1
        else:
            screen.blit(pygame.image.load(f'assets/credits_gif_frames/frame_{gif_frame}.png'), (0,0))
            gif_frame = 0
            
        pygame.time.delay(30)
        
        
        # back text
        if 75 <= mouse[0] <= 225 and 620 <= mouse[1] <= 680:
            drawRhomboid(screen, red, white, 75, 620, 150, 60, 30, 5)
        else:
            drawRhomboid(screen, red, red, 75, 620, 150, 60, 30, 5)
        screen.blit(back_text, (75 + 12.5 + (150 - back_text.get_width())/2, 620 + 12.5))

        pygame.display.update()



def how_to_play():
    """How To Play Screen

    This function displays the how to play screen of the Turbo Racing 3000 game.
    It loads and displays the how to play image, plays the how to play soundtrack, and handles user input for the back button.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    
    
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    
    # creating some important colors
    white = (255, 255, 255)
    red = (255, 0, 0)

    width = screen.get_width()
    height = screen.get_height()

    # creating buttons text label
    font = pygame.font.Font('fonts/MASQUE__.ttf', 28)
    back_text = font.render('Back', True, white)
    
    # Play credits soundtrack
    pygame.mixer.music.load('assets/howtoplay_soundtrack.mp3')
    pygame.mixer.music.play(-1)

    # Create the infinite scrolling background for the menu
    MAP = pygame.image.load("assets/infinite_level.png").convert_alpha()
    MAP = pygame.transform.scale_by(MAP, 0.9)
    mapY0 = -200
    mapY1 = -1280

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

        screen.blit(pygame.image.load('assets/howtoplay.png'), [0, 0, width, height])

        # back text
        if 75 <= mouse[0] <= 225 and 620 <= mouse[1] <= 680:
            drawRhomboid(screen, red, white, 75, 620, 150, 60, 30, 5)
        else:
            drawRhomboid(screen, red, red, 75, 620, 150, 60, 30, 5)
        screen.blit(back_text, (75 + 12.5 + (150 - back_text.get_width())/2, 620 + 12.5))

        pygame.display.update()

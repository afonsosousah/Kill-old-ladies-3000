from interface import *
global selected_car
global speed
global active_power_up

def main():
    pygame.init()
    
    # Play game soundtrack
    #pygame.mixer.music.load('assets/game_soundtrack.mp3')
    #pygame.mixer.music.play(-1)
    
    # Go to main menu
    interface()

if __name__ == '__main__':
    main()
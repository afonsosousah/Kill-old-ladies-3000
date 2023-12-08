from interface import *
global selected_car
global selected_car2
global speed
global MAP_BORDER_MASK 
global all_coming_cars
global slowing_active


def main():
    pygame.init()
    
    # Play game soundtrack
    #pygame.mixer.music.load('assets/game_soundtrack.mp3')
    #pygame.mixer.music.play(-1s)
    
    # Go to main menu
    interface()

if __name__ == '__main__':
    main()
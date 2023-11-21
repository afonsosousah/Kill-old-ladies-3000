import pygame, random
# Let's import the Car class and the Map class
from car import Car
from map import Map
import main
import interface

def car_racing():
    pygame.init()

    GREEN = (20, 255, 140)
    GREY = (210, 210 ,210)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
    YELLOW = (253, 199, 79)
    CYAN = (0, 255, 255)
    BLUE = (100, 100, 255)

    speed = 1
    colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)
    car_crash = False

    SCREENWIDTH=800
    SCREENHEIGHT=600

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Turbo Racing 3000")

    # creating map
    MAP = pygame.image.load("assets/infinite_level.png").convert_alpha()
    MAP_BORDER = pygame.image.load("assets/map_border.png")
    MAP_BORDER_MASK = pygame.mask.from_surface(MAP_BORDER)

    # creating buttons text labels
    corbelfont = pygame.font.SysFont('Corbel', 40, bold=True, italic=True)
    play_text = corbelfont.render('Play', True, WHITE)
    back_text = corbelfont.render('Back', True, WHITE)

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()


    playerCar = Car(RED, 60, 80, 70, main.selected_car, False)
    playerCar.rect.x = SCREENWIDTH/2 - 60/2
    playerCar.rect.y = SCREENHEIGHT - 110

    car1 = Car(PURPLE, 60, 80, random.randint(50,100), random.randint(1,6))
    car1.rect.x = 195
    car1.rect.y = -100

    car2 = Car(YELLOW, 60, 80, random.randint(50,100), random.randint(1,6))
    car2.rect.x = 315
    car2.rect.y = -600

    car3 = Car(CYAN, 60, 80, random.randint(50,100), random.randint(1,6))
    car3.rect.x = 435
    car3.rect.y = -300

    car4 = Car(BLUE, 60, 80, random.randint(50,100), random.randint(1,6))
    car4.rect.x = 555
    car4.rect.y = -1000
    
    car5 = Car(GREY, 60, 80, random.randint(50,100), random.randint(1,6))
    car5.rect.x = 675
    car5.rect.y = -400


    # Game background
    map1 = Map(SCREENWIDTH, SCREENHEIGHT*2, 25)
    map2 = Map(SCREENWIDTH, SCREENHEIGHT*2, 25)
    # put the second map above the first
    map1.rect.y = 600
    map2.rect.y = -600
    
    # Add maps to list of objects
    all_sprites_list.add(map1)
    all_sprites_list.add(map2)
    
    maps_group = pygame.sprite.Group()
    maps_group.add(map1)
    maps_group.add(map2)


    # Add the car to the list of objects
    all_sprites_list.add(playerCar)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)


    # Allowing the user to close the window...
    carryOn = True
    clock=pygame.time.Clock()
    

    while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                    pygame.quit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                         playerCar.moveRight(10)
                # Press the back button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(mouse[0])
                    print(mouse[1])
                    if 150 <= mouse[0] <= 300 and 500 <= mouse[1] <= 560:
                        carryOn = False
                        interface.interface()
                # Pressing the play button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 400 <= mouse[0] <= 550 and 500 <= mouse[1] <= 560:
                        car_racing()

            # Not letting the car go off the road
            if playerCar.collide(MAP_BORDER_MASK) != None:
                playerCar.bounce()

            keys = pygame.key.get_pressed()
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not car_crash:
                playerCar.moveLeft(8)
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not car_crash:
                playerCar.moveRight(8)
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and not car_crash:
                if speed + 0.05 < 3: # setting max speed
                    speed += 0.05
            if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not car_crash:
                if speed - 0.05 > 0.5: # setting min speed
                    speed -= 0.05


            # Pixel perfect collision betwee cars
            player_car_mask = playerCar.create_mask()

            for car in all_coming_cars:
                coming_cars_masks = car.create_mask()
                offset = (int(car.rect.x - playerCar.rect.x), int(car.rect.y - playerCar.rect.y))

                collision_point = player_car_mask.overlap(coming_cars_masks, offset)

                if collision_point:
                    print("Collision!")


            # Game Logic
            for car in all_coming_cars:
                car.moveForward(speed)
                if car.rect.y > SCREENHEIGHT:
                    car.changeSpeed(random.randint(50,100))
                    car.repaint(random.choice(colorList))
                    car.rect.y = -200

                # Check if there is a car collision
                car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
                for car in car_collision_list:
                    print("Car crash!")
                    car_crash = True
          
                      
            # Infinite scrolling map

            if map2.rect.y > -400 and map2.rect.y < -100:
                map1.rect.y = 100 + map2.rect.y - 1200

            if map1.rect.y > -400 and map1.rect.y < -100:
                map2.rect.y = 100 + map1.rect.y - 1200
                
            map1.moveDown(speed)
            map2.moveDown(speed)
                

            all_sprites_list.update()

            '''
            #Drawing on Screen
            screen.fill(GREEN)
            #Draw The Road
            pygame.draw.rect(screen, GREY, [40,0, 400,SCREENHEIGHT])
            #Draw Line painting on the road
            pygame.draw.line(screen, WHITE, [140,0],[140,SCREENHEIGHT],5)
            #Draw Line painting on the road
            pygame.draw.line(screen, WHITE, [240,0],[240,SCREENHEIGHT],5)
            #Draw Line painting on the road
            pygame.draw.line(screen, WHITE, [340,0],[340,SCREENHEIGHT],5)
            '''
            
            # load backgroud grass texture
            # screen.blit(pygame.image.load("assets/grass.png"), [0,0, SCREENWIDTH,SCREENHEIGHT])
            # load road
            # screen.blit(pygame.image.load("assets/road.png"), [0,0, SCREENWIDTH,SCREENHEIGHT])


            #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)
            
            if(car_crash):
                speed = 0
                screen.blit(pygame.image.load('assets/game_over.png'), [0, 0, SCREENWIDTH, SCREENHEIGHT])
                # play text
                mouse = pygame.mouse.get_pos()
                # when the mouse is on the box it changes color
                if 400 <= mouse[0] <= 550 and 560 <= mouse[1] <= 620:
                    interface.drawRhomboid(screen, YELLOW, YELLOW, 400, 500, 150, 60, 30, 5)
                else:
                    interface.drawRhomboid(screen, YELLOW, WHITE, 400, 500, 150, 60, 30, 5)
                screen.blit(play_text, (400 + (150 - play_text.get_width())/2, 500 + 10))
                
                # quit text
                if 150 <= mouse[0] <= 300 and 560 <= mouse[1] <= 620:
                    interface.drawRhomboid(screen, RED, RED, 150, 500, 150, 60, 30, 5)
                else:
                    interface.drawRhomboid(screen, RED, WHITE, 150, 500, 150, 60, 30, 5)
                screen.blit(back_text, (150 + (150 - back_text.get_width())/2, 500 + 10))
                

            #Refresh Screen
            pygame.display.flip()
                       

            #Number of frames per secong e.g. 60
            clock.tick(60)
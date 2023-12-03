'''import pygame, random
# Let's import the Car class and the Map class
from car import Car
from power_up import Power_Up
import main
import interface
import math

def multiplayer_racing():
    pygame.init()

    GREEN = (20, 255, 140)
    GREY = (210, 210 ,210)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    PURPLE = (255, 0, 255)
    YELLOW = (253, 199, 79)
    CYAN = (0, 255, 255)
    BLUE = (100, 100, 255)

    main.speed = 1
    main.active_power_up = None
    colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)
    car_crash = False

    SCREENWIDTH=800
    SCREENHEIGHT=600

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Turbo Racing 3000")

    # creating map
    # Game background
    MAP = pygame.image.load("assets/infinite_level.png").convert_alpha()
    MAP_BORDER = pygame.image.load("assets/map_border.png")
    MAP_BORDER_MASK = pygame.mask.from_surface(MAP_BORDER)
    mapY0 = 0
    mapY1 = -1200

    # Creating the score
    score_value = 0
    score_font = pygame.font.SysFont('Corbel', 25, bold = True)
    score_text = score_font.render("Score: " + str(score_value), True, (255, 255, 255))

    # creating buttons text labels
    corbelfont = pygame.font.SysFont('Corbel', 40, bold=True, italic=True)
    play_text = corbelfont.render('Play', True, WHITE)
    back_text = corbelfont.render('Back', True, WHITE)

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
    
    # Define where the enemies spawn
    carSpawnLocationsX = (195, 315, 435, 555) # spawn in each lane of the map 

    playerCar1 = Car(RED, 60, 80, 70, main.selected_car, False)
    playerCar1.rect.x = SCREENWIDTH/2 - 60/2
    playerCar1.rect.y = SCREENHEIGHT - 110

    playerCar2 = Car(BLUE, 60, 80, 70, main.selected_car, False)
    playerCar2.rect.x = SCREENWIDTH/2 - 60/2
    playerCar2.rect.y = SCREENHEIGHT - 100



    car1 = Car(PURPLE, 60, 80, random.randint(50,100), random.randint(1,6))
    car1.rect.x = carSpawnLocationsX[0]
    car1.rect.y = -100

    car2 = Car(YELLOW, 60, 80, random.randint(50,100), random.randint(1,6))
    car2.rect.x = carSpawnLocationsX[1]
    car2.rect.y = -600

    car3 = Car(CYAN, 60, 80, random.randint(50,100), random.randint(1,6))
    car3.rect.x = carSpawnLocationsX[2]
    car3.rect.y = -300

    car4 = Car(BLUE, 60, 80, random.randint(50,100), random.randint(1,6))
    car4.rect.x = carSpawnLocationsX[3]
    car4.rect.y = -1000
    

    # Add the cars to the list of objects
    all_sprites_list.add(playerCar1)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)

    all_sprites_list.add(playerCar2)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)

    # Create a list of the enemy cars
    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)
    
    
    
    # Define where the power ups spawn
    powerUpSpawnLocationsX = (250, 390, 500)  # spawn in the middle of the lanes
    
    # Define what are the available types of power ups
    powerUpTypes = ("invincibility", "slowing", "repaint", "random")
    
    # Creating the Power Ups
    powerUp1 = Power_Up(random.choice(powerUpTypes), random.randint(50,100))
    powerUp1.rect.x = random.choice(powerUpSpawnLocationsX)
    powerUp1.rect.y = -300
    
    # Create a list of all Power Ups
    all_power_ups = pygame.sprite.Group()
    all_power_ups.add(powerUp1)
    all_sprites_list.add(powerUp1)



    # Allowing the user to close the window...
    carryOn = True
    clock=pygame.time.Clock()
    wait_for_key = True


    while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                    pygame.quit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                         playerCar1.moveRight(10)
                # Press the back button
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 195 <= mouse[0] <= 345 and 500 <= mouse[1] <= 560:
                        carryOn = False
                        interface.interface()
                # Pressing the play button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 445 <= mouse[0] <= 595 and 500 <= mouse[1] <= 560:
                        multiplayer_racing()               
            

            # Infinite scrolling map
            screen.blit(MAP, [0, mapY0, SCREENWIDTH, SCREENHEIGHT*2])
            screen.blit(MAP, [0, mapY1, SCREENWIDTH, SCREENHEIGHT*2])
            if mapY0 > -300:
                mapY1 = mapY0 - 1200
            if mapY1 > -300:
                mapY0 = mapY1 - 1200
            # move the map 
            mapY0 += main.speed * 2
            mapY1 += main.speed * 2

            # Drawing the score
            score_text = score_font.render("Score: " + str(score_value), True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            # Not letting the car go off the road
            if playerCar1.collide(MAP_BORDER_MASK) != None:
                playerCar1.bounce()

            if playerCar2.collide(MAP_BORDER_MASK) != None:
                playerCar2.bounce()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and not car_crash:
                playerCar1.moveLeft(8)
            if keys[pygame.K_RIGHT] and not car_crash:
                playerCar1.moveRight(8)
            if keys[pygame.K_UP] and not car_crash:
                # setting max speed and not letting speed up if slowing power up
                if main.speed + 0.05 < 2 \
                    and not (main.active_power_up != None and main.active_power_up.typeWhenActivated == "slowing"):
                    main.speed += 0.05
            if keys[pygame.K_DOWN] and not car_crash:
                # setting min speed and not letting speed down if slowing power up
                if main.speed - 0.05 > 1 \
                    and not(main.active_power_up != None and main.active_power_up.typeWhenActivated == "slowing"):
                    main.speed -= 0.05

            if keys[pygame.K_a] and not car_crash:
                playerCar2.moveLeft(8)
            if keys[pygame.K_d] and not car_crash:
                playerCar2.moveRight(8)
            if keys[pygame.K_w] and not car_crash:
                # setting max speed and not letting speed up if slowing power up
                if main.speed + 0.05 < 2 \
                    and not (main.active_power_up != None and main.active_power_up.typeWhenActivated == "slowing"):
                    main.speed += 0.05
            if keys[pygame.K_s] and not car_crash:
                # setting min speed and not letting speed down if slowing power up
                if main.speed - 0.05 > 1 \
                    and not(main.active_power_up != None and main.active_power_up.typeWhenActivated == "slowing"):
                    main.speed -= 0.05

            # Pixel perfect collision between cars and powerups
            player_car1_mask = playerCar1.create_mask()
            player_car2_mask = playerCar2.create_mask()

            for car in all_coming_cars:
                coming_cars_masks = car.create_mask()
                offset = (int(car.rect.x - playerCar1.rect.x), int(car.rect.y - playerCar1.rect.y))
                collision_point = player_car1_mask.overlap(coming_cars_masks, offset)

            for car in all_coming_cars:
                coming_cars_masks = car.create_mask()
                offset = (int(car.rect.x - playerCar2.rect.x), int(car.rect.y - playerCar2.rect.y))
                collision_point = player_car2_mask.overlap(coming_cars_masks, offset)

                if collision_point:
                    car_crash = True
                    #print("Collision!")
            
            for powerUp in all_power_ups:
                powerUpMask = powerUp.create_mask()
                offset = (int(powerUp.rect.x - playerCar1.rect.x), int(powerUp.rect.y - playerCar1.rect.y))
                collision_point = player_car1_mask.overlap(powerUpMask, offset)

            for powerUp in all_power_ups:
                powerUpMask = powerUp.create_mask()
                offset = (int(powerUp.rect.x - playerCar2.rect.x), int(powerUp.rect.y - playerCar2.rect.y))
                collision_point = player_car2_mask.overlap(powerUpMask, offset)

                if collision_point:
                    print("Collision with powerup!")
                    powerUp.affectPlayer(playerCar1)
                    powerUp.changeSpeed(random.randint(50, 70))
                    powerUp.repaint(random.choice(powerUpTypes))
                    powerUp.rect.y = random.randint(-1000, -100)
                    powerUp.rect.x = random.choice(powerUpSpawnLocationsX)
                    
                if collision_point:
                    print("Collision with powerup!")
                    powerUp.affectPlayer(playerCar2)
                    powerUp.changeSpeed(random.randint(50, 70))
                    powerUp.repaint(random.choice(powerUpTypes))
                    powerUp.rect.y = random.randint(-1000, -100)
                    powerUp.rect.x = random.choice(powerUpSpawnLocationsX)  # move to any of the spawn locations


            # Game Logic
            for car in all_coming_cars:
                car.moveForward(main.speed)
                if car.rect.y > SCREENHEIGHT:
                    car.changeSpeed(random.randint(50,100))
                    car.repaint()
                    car.rect.y = random.randint(-1000, -100)
                    score_value += 1
            
            # Power Ups
            for powerUp in all_power_ups:
                powerUp.moveForward(main.speed)
                if powerUp.rect.y > 3*SCREENHEIGHT:  # we are multiplying by 3 to spawn 3 times less powerups than cars
                    powerUp.changeSpeed(random.randint(50, 70))
                    powerUp.repaint(random.choice(powerUpTypes))
                    powerUp.rect.y = random.randint(-1000, -100)
                    powerUp.rect.x = random.choice(powerUpSpawnLocationsX)  # move to any of the spawn locations
            
            # Check if there is any active power up to deactivate
            if main.active_power_up != None:
                if pygame.time.get_ticks() - main.active_power_up.startTime >= main.active_power_up.timeout:
                    main.active_power_up.deactivate()
            
            
            
            all_sprites_list.update()

            # Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
            all_sprites_list.draw(screen)

            # Wait for key press to start
            if(wait_for_key):
                main.speed = 0
                msToChange = 500  # We set the amount of milliseconds that each frame stays
                if (pygame.time.get_ticks() // msToChange) % 2 == 0:
                    screen.blit(pygame.image.load('assets/press_any_key.png'), [0, 0, SCREENWIDTH, SCREENHEIGHT])
                else:
                    screen.blit(pygame.image.load('assets/press_any_key_empty.png'), [0, 0, SCREENWIDTH, SCREENHEIGHT])
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        wait_for_key = False
                        main.speed = 1
            
            # Game over menu
            if(car_crash):
                main.speed = 0
                screen.blit(pygame.image.load('assets/game_over.png'), [0, 0, SCREENWIDTH, SCREENHEIGHT])
                # play text
                mouse = pygame.mouse.get_pos()
                # when the mouse is on the box it changes color
                if 445 <= mouse[0] <= 595 and 500 <= mouse[1] <= 560:
                    interface.drawRhomboid(screen, YELLOW, WHITE, 445, 500, 150, 60, 30, 5)
                else:
                    interface.drawRhomboid(screen, YELLOW, YELLOW, 445, 500, 150, 60, 30, 5)
                screen.blit(play_text, (445 + 12.5 + (150 - play_text.get_width())/2, 500 + 12.5))
                
                # quit text
                if 195 <= mouse[0] <= 345 and 500 <= mouse[1] <= 560:
                    interface.drawRhomboid(screen, RED, WHITE, 195, 500, 150, 60, 30, 5)
                else:
                    interface.drawRhomboid(screen, RED, RED, 195, 500, 150, 60, 30, 5)
                screen.blit(back_text, (195 + 12.5 + (150 - back_text.get_width())/2, 500 + 12.5))
                

            #Refresh Screen
            pygame.display.flip()
                       

            #Number of frames per secong e.g. 60
            clock.tick(60)'''
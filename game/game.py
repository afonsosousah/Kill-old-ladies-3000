import pygame, random
# Let's import the Car class and the Map class
from car import Car
from power_up import PowerUp
from fuel_can import FuelCan
import main
import interface
import math

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
    main.MAP_BORDER_MASK = pygame.mask.from_surface(MAP_BORDER)
    mapY0 = 0
    mapY1 = -1200

    # Creating the score
    score_background = pygame.image.load("assets/score_background.png").convert_alpha()
    score_background = pygame.transform.scale(score_background, (80,47))
    score_value = 0
    score_font = pygame.font.SysFont('Corbel', 20, bold = True)
    score_text = score_font.render("Score: " + str(score_value), True, (255, 255, 255))

    # Creating the high score
    previous_score = 0
    high_score = 0

    # Creating the score and highscore for the game over menu
    score_font_gameover = pygame.font.SysFont('Corbel', 35, bold = True)
    score_background_gameover = pygame.image.load("assets/score_background_gameover.png").convert_alpha()
    score_background_gameover = pygame.transform.scale(score_background_gameover, (150,81))

    highscore_background = pygame.image.load("assets/highscore_background.png").convert_alpha()
    highscore_background_gameover = pygame.transform.scale(highscore_background, (150,81))

    # Creating the speedometer
    speedometer = pygame.image.load("assets/speedometer.png").convert_alpha()
    speedometer = pygame.transform.scale(speedometer, (120, 120))

    # Creating the speedmeter pointer
    pointer = pygame.image.load("assets/pointer.png").convert_alpha()
    pointer = pygame.transform.scale(pointer, (120, 120))

    # Creating the gasmeter
    gasmeter = pygame.image.load("assets/gasmeter.png").convert_alpha()
    gasmeter = pygame.transform.scale(gasmeter, (120, 120))

    # Creating the gasmeter pointer
    gas_pointer = pygame.image.load("assets/gas_pointer.png").convert_alpha()
    gas_pointer = pygame.transform.scale(gas_pointer, (120, 120))

    # Creating the pause button
    pause = False
    pause_button = pygame.image.load("assets/pause.png")
    pause_button = pygame.transform.scale(pause_button, (50,50))

    # creating buttons text labels
    corbelfont = pygame.font.SysFont('Corbel', 40, bold=True, italic=True)
    play_text = corbelfont.render('Play', True, WHITE)
    back_text = corbelfont.render('Back', True, WHITE)
    resume_text = corbelfont.render('Resume', True, WHITE)
    quit_text = corbelfont.render('Quit', True, WHITE)

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
    
    # Define where the enemies spawn
    carSpawnLocationsX = (195, 315, 435, 555) # spawn in each lane of the map

    playerCar = Car(RED, 60, 80, 70, main.selected_car, False)
    playerCar.rect.x = SCREENWIDTH/2 - 60/2
    playerCar.rect.y = SCREENHEIGHT - 110

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
    

    # Add the car to the list of objects
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)
    all_sprites_list.add(playerCar)

    # Create a list of the enemy cars
    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)
    
    
    
    # Define where the power ups spawn
    powerUpSpawnLocationsX = (250, 390, 500)  # spawn in the middle of the lanes
    
    # Define what are the available types of power ups
    powerUpTypes = ("invincibility", "slowing", "repaint", "random", "invisibility")
    
    # Creating the Power Ups
    powerUp1 = PowerUp(random.choice(powerUpTypes), random.randint(50,100))
    powerUp1.rect.x = random.choice(powerUpSpawnLocationsX)
    powerUp1.rect.y = -300
    
    # Create a list of all Power Ups
    all_power_ups = pygame.sprite.Group()
    all_power_ups.add(powerUp1)
    all_sprites_list.add(powerUp1)
    
    
    # Creating the Fuel Can
    fuel_can = FuelCan(1)
    fuel_can.rect.x = random.choice(powerUpSpawnLocationsX)
    fuel_can.rect.y = -200

    all_sprites_list.add(fuel_can)
    

    # Allowing the user to close the window...
    carryOn = True
    clock=pygame.time.Clock()
    wait_for_key = True
    
    # Set the initial fuel level (1.0 represents a full tank)
    playerCar.fuel_level = 1.0

    # Initial settings for Low Fuel warning
    low_fuel_threshold = 0.2
    blinking_interval = 500
    is_low_fuel = False
    blink_visible = True
    last_blink_time = pygame.time.get_ticks()

    # Play game soundtrack
    #pygame.mixer.music.load('assets/game_soundtrack.mp3')
    #pygame.mixer.music.play(-1)


    while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                    pygame.quit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                         playerCar.moveRight(10)

                # Press the back button
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 195 <= mouse[0] <= 345 and 500 <= mouse[1] <= 560:
                        carryOn = False
                        interface.interface()
                        
                # Pressing the play button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 445 <= mouse[0] <= 595 and 500 <= mouse[1] <= 560:
                        if pause:
                            pause = False
                        elif car_crash:
                            car_racing()
                            
                # Pressing the pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 725 <= mouse[0] <= 775 and 15 <= mouse[1] <= 65:
                        # Using the pause button to pause and resume the game (while we don't have the pause menu)
                        # if pause:
                            # pause = False
                            # print("Game Resumed!") 
                        # else:
                            pause = True
                            print("Game Paused!")
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        # You can pause and resume the game by pressing 'esc'
                        if pause:
                            pause = False
                            print("Game Resumed!") 
                        else:
                            pause = True
                            print("Game Paused!")
                            
                # Stop moving to the sides after the key is released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                        playerCar.side_speed = 0
            

            # Infinite scrolling map
            screen.blit(MAP, [0, mapY0, SCREENWIDTH, SCREENHEIGHT*2])
            screen.blit(MAP, [0, mapY1, SCREENWIDTH, SCREENHEIGHT*2])
            if mapY0 > -300:
                mapY1 = mapY0 - 1200
            if mapY1 > -300:
                mapY0 = mapY1 - 1200
            # move the map 
            if(not pause):
                mapY0 += main.speed * 2
                mapY1 += main.speed * 2

            # Drawing the score
            screen.blit(score_background, (10, 10))
            score_text = score_font.render(str(score_value), True, (255, 255, 255))
            screen.blit(score_text, (45, 32))

            # Drawing the pause button
            screen.blit(pause_button, (725,15))

            # Not letting the car go off the road
            if playerCar.collide(main.MAP_BORDER_MASK) != None:
                playerCar.bounce()

            if(not pause):
                keys = pygame.key.get_pressed()
                if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not car_crash and main.speed != 0:
                    playerCar.moveLeft(8)
                if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not car_crash and main.speed != 0:
                    playerCar.moveRight(8)
                if (keys[pygame.K_UP] or keys[pygame.K_w]) and not car_crash:
                    # setting max speed (120kph) and not letting speed up if slowing power up
                    if math.floor((main.speed + 0.03) * 50) <= 270 \
                        and not (main.active_power_up != None and main.active_power_up.typeWhenActivated == "slowing"):
                        main.speed += 0.03
                if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not car_crash:
                    # setting min speed (50kph) and not letting speed down if slowing power up
                    if math.floor((main.speed - 0.05) * 50) >= 30 \
                        and not(main.active_power_up != None and main.active_power_up.typeWhenActivated == "slowing"):
                        main.speed -= 0.05


            # Create the player mask for the collisions
            player_car_mask = playerCar.create_mask()

            ''' Pixel perfect collision between player and cars '''
            for car in all_coming_cars:
                coming_cars_masks = car.create_mask()
                offset = (int(car.rect.x - playerCar.rect.x), int(car.rect.y - playerCar.rect.y))
                collision_point = player_car_mask.overlap(coming_cars_masks, offset)
                if collision_point and playerCar.invincible:
                    # Respawn the car and make it disappear
                    car.changeSpeed(random.randint(50,100))
                    car.repaint()
                    car.rect.y = random.randint(-1000, -100)
                    score_value += 1
                elif collision_point and playerCar.invisible:
                    # Just go over the car
                    score_value += 1
                elif collision_point:
                    car_crash = True
                    print("Collision!")

        
            ''' Pixel perfect collision between player and powerups '''
            if(not pause):
                for powerUp in all_power_ups:
                    powerUpMask = powerUp.create_mask()
                    offset = (int(powerUp.rect.x - playerCar.rect.x), int(powerUp.rect.y - playerCar.rect.y))
                    collision_point = player_car_mask.overlap(powerUpMask, offset)
                    if collision_point:
                        print("Collision with powerup!")
                        powerUp.affectPlayer(playerCar)
                        powerUp.changeSpeed(random.randint(50, 70))
                        powerUp.repaint(random.choice([pwrup for pwrup in powerUpTypes if pwrup != powerUp.type])) # Repaint to a different power up
                        powerUp.rect.y = random.randint(-1500, -500)
                        powerUp.rect.x = random.choice(powerUpSpawnLocationsX)  # move to any of the spawn locations


            ''' Pixel perfect collision between player and fuel cans '''
            if not pause:
                fuelCanMask = fuel_can.create_mask()
                offset = (int(fuel_can.rect.x - playerCar.rect.x), int(fuel_can.rect.y - playerCar.rect.y))
                collision_point = player_car_mask.overlap(fuelCanMask, offset)
                if collision_point:
                    print("Collision with fuel can!")
                    playerCar.refuel()
                    # respawn the fuel can
                    fuel_can.rect.y = random.randint(-2000, -1000)
                    # move to any of the spawn locations different to the current one
                    fuel_can.rect.x = random.choice([loc for loc in powerUpSpawnLocationsX if loc != fuel_can.rect.x])


            ''' Respawn cars '''
            if(not pause):
                for car in all_coming_cars:
                    car.moveForward(main.speed)
                    if car.rect.y > SCREENHEIGHT:
                        car.changeSpeed(random.randint(50,100))
                        car.repaint()
                        car.rect.y = random.randint(-1000, -100)
                        score_value += 1
                        gameover_score_value = score_value
            
            
            ''' Respawn power ups '''
            if(not pause):
                for powerUp in all_power_ups:
                    powerUp.moveForward(main.speed)
                    if powerUp.rect.y > 3*SCREENHEIGHT:  # we are multiplying by 3 to spawn 3 times less powerups than cars
                        powerUp.changeSpeed(random.randint(50, 70))
                        powerUp.repaint(random.choice([pwrup for pwrup in powerUpTypes if pwrup != powerUp.type])) # Repaint to a different power up
                        powerUp.rect.y = random.randint(-1500, -500)
                        powerUp.rect.x = random.choice(powerUpSpawnLocationsX)  # move to any of the spawn locations
                        
            
            ''' Respawn fuel cans'''
            if not pause:
                fuel_can.moveForward(main.speed)
                if fuel_can.rect.y > SCREENHEIGHT * 2: # we are multiplying by 2 to spawn 2 times less fuel cans than cars
                    fuel_can.rect.y = random.randint(-300, -50)
                    # move to any of the spawn locations different to the current one
                    fuel_can.rect.x = random.choice([loc for loc in powerUpSpawnLocationsX if loc != fuel_can.rect.x])
            
            
            ''' Power up logic '''
            if(not pause):
                if main.active_power_up != None:
                    # Display remaining power up time
                    if ((main.active_power_up.timeout - (pygame.time.get_ticks() - main.active_power_up.startTime)) > 0 and
                        main.active_power_up.typeWhenActivated != "repaint"):
                        powerUpTimer_background = pygame.image.load("assets/timer_background.png").convert_alpha()
                        powerUpTimer_value = round((main.active_power_up.timeout - (pygame.time.get_ticks() - main.active_power_up.startTime)) / 1000, 1)
                        powerUpTimer_font = pygame.font.SysFont('Corbel', 23, bold = True)
                        powerUpTimer_text = powerUpTimer_font.render(str(powerUpTimer_value) + "s", True, (0,0,0))
                        screen.blit(powerUpTimer_background, (0, 120 - (powerUpTimer_background.get_height() // 2)))
                        screen.blit(powerUpTimer_text, ((powerUpTimer_background.get_width() // 2) - (powerUpTimer_text.get_width() // 2), 120 - (powerUpTimer_text.get_height() // 2) + 5))

                    # Disable power up after the timeout
                    if pygame.time.get_ticks() - main.active_power_up.startTime >= main.active_power_up.timeout:
                        main.active_power_up.deactivate(playerCar)
            
            
            ''' Draw the sprites '''
            all_sprites_list.update()
            # Now let's draw all the sprites in one go.
            all_sprites_list.draw(screen)
            
            
            ''' Speedometer '''
            # Defining the position of the speedometer and calculating the angle for the pointer
            speedometer_rect = (660, 460, speedometer.get_rect().x, speedometer.get_rect().y)
            angle = math.floor(main.speed * 50) # convert the speed

            # Rotate the pointer around its base
            rotated_pointer = pygame.transform.rotate(pointer, -angle)
            pointer_rect = rotated_pointer.get_rect()

            # The pivot should be the center of the speedometer
            pivot = (speedometer_rect[0] + (speedometer.get_width() // 2), speedometer_rect[1] + (speedometer.get_height() // 2) + 2)

            # Calculate the new center of the rotated pointer image
            rotated_pointer_center = (pivot[0] - (pointer_rect.width // 2), pivot[1] - (pointer_rect.height // 2))

            # Drawing the speedometer and the pointer
            screen.blit(speedometer, speedometer_rect)
            screen.blit(rotated_pointer, rotated_pointer_center)


            ''' Gasmeter '''
            if(not pause):
                # Update fuel level and ensure doesn't go below 0
                playerCar.fuel_level -= 0.0005 * main.speed  # make the fuel depend on the speed
                playerCar.fuel_level = max(playerCar.fuel_level, 0)


            # Defining the position of the gasmeter and calculating the angle for the pointer
            gasmeter_rect = (20, 460, gasmeter.get_rect().x, gasmeter.get_rect().y)
            gas_angle = -282 * (1 - playerCar.fuel_level)

            # Rotate the pointer around its base
            rotated_gas_pointer = pygame.transform.rotate(gas_pointer, -gas_angle)
            gas_pointer_rect = rotated_gas_pointer.get_rect()

            # The pivot should be the center of the gasmeter
            pivot = (gasmeter_rect[0] + (gasmeter.get_width() // 2), gasmeter_rect[1] + (gasmeter.get_height() // 2) + 2)

            # Calculate the new center of the rotated pointer image
            rotated_gas_pointer_center = (pivot[0] - (gas_pointer_rect.width // 2), pivot[1] - (gas_pointer_rect.height // 2))

            # Drawing the gasmeter and the pointer
            screen.blit(gasmeter, gasmeter_rect)
            screen.blit(rotated_gas_pointer, rotated_gas_pointer_center)

            ''' Low Fuel Warning'''
            # Load font for Low Fuel message
            font = pygame.font.SysFont('Corbel', 25, bold = True) 
            low_fuel_text = font.render('Low Fuel!', True, pygame.Color('RED'))
            low_fuel_rect = low_fuel_text.get_rect(center=(80, 440))

            # Update the Low Fuel state
            if playerCar.fuel_level < low_fuel_threshold:
                is_low_fuel = True
            else:
                is_low_fuel = False

            # Blink Low Fuel message if the state is active
            if is_low_fuel:
                current_time = pygame.time.get_ticks()
                if current_time - last_blink_time > blinking_interval:
                    blink_visible = not blink_visible
                    last_blink_time = current_time

                if blink_visible:
                    screen.blit(low_fuel_text, low_fuel_rect)

            # Check if there is a collision with a fuel can
            collision_point = player_car_mask.overlap(fuelCanMask, offset)
            if collision_point:
                is_low_fuel = False

            ''' Wait for key press to start '''
            if(wait_for_key):
                main.speed = 0
                
                # Make the Press any key to start text blink
                msToChange = 500  # We set the amount of milliseconds that each frame stays
                if (pygame.time.get_ticks() // msToChange) % 2 == 0:
                    screen.blit(pygame.image.load('assets/press_any_key.png'), [0, 0, SCREENWIDTH, SCREENHEIGHT])
                else:
                    screen.blit(pygame.image.load('assets/empty.png'), [0, 0, SCREENWIDTH, SCREENHEIGHT])
                
                # If the key gets pressed, start the game
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        wait_for_key = False
                        main.speed = 1


            ''' Pause menu '''
            if(pause):
                # Make the Game Paused text blink
                msToChange = 500  # We set the amount of milliseconds that each frame stays
                if (pygame.time.get_ticks() // msToChange) % 2 == 0:
                    screen.blit(pygame.image.load('assets/game_paused.png'), [0, 0, SCREENWIDTH, SCREENHEIGHT])
                else:
                    screen.blit(pygame.image.load('assets/empty.png'), [0, 0, SCREENWIDTH, SCREENHEIGHT])
                
                # Draw the buttons
                mouse = pygame.mouse.get_pos()
                # play text
                # when the mouse is on the box it changes color
                if 445 <= mouse[0] <= 595 and 500 <= mouse[1] <= 560:
                    interface.drawRhomboid(screen, YELLOW, WHITE, 445, 500, 150, 60, 30, 5)
                else:
                    interface.drawRhomboid(screen, YELLOW, YELLOW, 445, 500, 150, 60, 30, 5)
                screen.blit(resume_text, (448 + 12.5 + (150 - resume_text.get_width())/2, 500 + 12.5))
                
                # quit text
                if 195 <= mouse[0] <= 345 and 500 <= mouse[1] <= 560:
                    interface.drawRhomboid(screen, RED, WHITE, 195, 500, 150, 60, 30, 5)
                else:
                    interface.drawRhomboid(screen, RED, RED, 195, 500, 150, 60, 30, 5)
                screen.blit(quit_text, (195 + 12.5 + (150 - quit_text.get_width())/2, 500 + 12.5))
            
            
            ''' Game over menu '''
            if(car_crash) or (playerCar.fuel_level == 0):
                # Stop the cars
                main.speed = 0
                
                #pygame.mixer.music.stop()
                
                # Show the Game Over art
                score_text_gameover = score_font_gameover.render(str(gameover_score_value), True, (255, 255, 255))

                screen.blit(pygame.image.load('assets/game_over.png'), [0, 0, SCREENWIDTH, SCREENHEIGHT])
                screen.blit(score_background_gameover, (220, 325))
                screen.blit(score_text_gameover, (285, 362))
                
                screen.blit(highscore_background_gameover, (450, 325))
                
                # Draw the buttons
                mouse = pygame.mouse.get_pos()
                # play text
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
                

            # Refresh Screen
            pygame.display.flip()
                       

            # Number of frames per secong e.g. 60
            clock.tick(60)
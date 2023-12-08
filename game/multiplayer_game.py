import pygame, random
# Let's import the Car class and the Map class
from car import Car
from power_up import Invincibility, Slowing, Repaint, Invisibility
from fuel_can import FuelCan
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

    playerCar1 = Car(60, 80, 70, main.selected_car, False)
    playerCar1.rect.x = SCREENWIDTH/2 - 60
    playerCar1.rect.y = SCREENHEIGHT - 110

    playerCar2 = Car(60, 80, 70, main.selected_car2, False)
    playerCar2.rect.x = SCREENWIDTH/2 + 60
    playerCar2.rect.y = SCREENHEIGHT - 110

    car1 = Car(60, 80, random.randint(50,100), random.randint(1,6))
    car1.rect.x = carSpawnLocationsX[0]
    car1.rect.y = -100

    car2 = Car(60, 80, random.randint(50,100), random.randint(1,6))
    car2.rect.x = carSpawnLocationsX[1]
    car2.rect.y = -600

    car3 = Car(60, 80, random.randint(50,100), random.randint(1,6))
    car3.rect.x = carSpawnLocationsX[2]
    car3.rect.y = -300

    car4 = Car(60, 80, random.randint(50,100), random.randint(1,6))
    car4.rect.x = carSpawnLocationsX[3]
    car4.rect.y = -1000
    

    # Add the car to the list of objects
    all_sprites_list.add(car1, car2, car3, car4)
    all_sprites_list.add(playerCar1, playerCar2)

    # Create a list of the enemy cars
    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1, car2, car3, car4)
    
    
    # Define where the power ups spawn
    powerUpSpawnLocationsX = (250, 390, 500)  # spawn in the middle of the lanes
    
    # Define what are the available types of power ups, and their weights
    powerUpTypes = [Invincibility, Slowing, Repaint, Invisibility]
    powerUpWeights = [15, 25, 20, 10]
    #powerUpTypes = ("invincibility", "slowing", "repaint", "random", "invisibility")
    
    # Creating the Power Ups
    powerUp1 = random.choices(powerUpTypes, powerUpWeights)[0](random.randint(50, 70))  # Select a PowerUp based on the weights 
    powerUp1.rect.x = random.choice(powerUpSpawnLocationsX)
    powerUp1.rect.y = -300
    
    powerUp2 = random.choices(powerUpTypes, powerUpWeights)[0](random.randint(50, 70))  # Select a PowerUp based on the weights 
    powerUp2.rect.x = random.choice(powerUpSpawnLocationsX)
    powerUp2.rect.y = -2000

    powerUp3 = random.choices(powerUpTypes, powerUpWeights)[0](random.randint(50, 70))  # Select a PowerUp based on the weights 
    powerUp3.rect.x = random.choice(powerUpSpawnLocationsX)
    powerUp3.rect.y = -3000
    
    # Create a list of all Power Ups
    all_power_ups = pygame.sprite.Group()
    all_power_ups.add(powerUp1, powerUp2, powerUp3)
    all_sprites_list.add(powerUp1, powerUp2, powerUp3)
    
    
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
    playerCar1.fuel_level = 1.0
    playerCar2.fuel_level = 1.0

    # Initial settings for Low Fuel warning
    low_fuel_threshold = 0.2
    blinking_interval = 500
    is_low_fuel_player1 = False
    is_low_fuel_player2 = False
    blink_visible = True
    last_blink_time = pygame.time.get_ticks()
    
    # Initialize game over reason variable
    game_over_reason = None

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
                         playerCar1.moveRight(10)
                         playerCar2.moveRight(10)
                         
                # Handle timeout of events   
                elif event.type==pygame.USEREVENT:
                    if playerCar1.activePowerUp:
                        playerCar1.activePowerUp.deactivate(playerCar1)
                    if playerCar2.activePowerUp:
                        playerCar2.activePowerUp.deactivate(playerCar2)

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
                            multiplayer_racing()
                            
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
                        playerCar1.side_speed = 0
                        playerCar2.side_speed = 0
            

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
            if playerCar1.collide(main.MAP_BORDER_MASK) != None:
                playerCar1.bounce()
            if playerCar2.collide(main.MAP_BORDER_MASK) != None:
                playerCar1.bounce()

            if(not pause):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and not car_crash:
                    playerCar2.moveLeft(8)
                if keys[pygame.K_RIGHT] and not car_crash:
                    playerCar2.moveRight(8)
                if keys[pygame.K_UP] and not car_crash:
                    # setting max speed (120kph) and not letting speed up if slowing power up
                    if math.floor((main.speed + 0.03) * 50) <= 270 \
                        and not playerCar2.slowing:
                        main.speed += 0.03
                if keys[pygame.K_DOWN] and not car_crash:
                    # setting min speed (50kph) and not letting speed down if slowing power up
                    if math.floor((main.speed - 0.05) * 50) >= 30 \
                        and not playerCar2.slowing:
                        main.speed -= 0.05
            
            if(not pause):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a] and not car_crash:
                    playerCar1.moveLeft(8)
                if keys[pygame.K_d] and not car_crash:
                    playerCar1.moveRight(8)
                if keys[pygame.K_w] and not car_crash:
                    # setting max speed (120kph) and not letting speed up if slowing power up
                    if math.floor((main.speed + 0.03) * 50) <= 270 \
                        and not playerCar1.slowing:
                        main.speed += 0.03
                if keys[pygame.K_s] and not car_crash:
                    # setting min speed (50kph) and not letting speed down if slowing power up
                    if math.floor((main.speed - 0.05) * 50) >= 30 \
                        and not playerCar1.slowing:
                        main.speed -= 0.05


            # Create the player mask for the collisions
            player_car_mask = playerCar1.create_mask()
            player_car2_mask = playerCar2.create_mask()

            ''' Pixel perfect collision between player and cars '''
            for car in all_coming_cars:
                coming_cars_masks = car.create_mask()

                # Car 1
                offset = (int(car.rect.x - playerCar1.rect.x), int(car.rect.y - playerCar1.rect.y))
                collision_point = player_car_mask.overlap(coming_cars_masks, offset)
                if collision_point and playerCar1.invincible:
                    # Respawn the car and make it disappear
                    car.changeSpeed(random.randint(50,100))
                    car.repaint()
                    car.rect.y = random.randint(-1000, -100)
                    score_value += 1
                elif collision_point and playerCar1.invisible:
                    # Just go over the car
                    score_value += 1
                elif collision_point:
                    car_crash = True
                    game_over_reason = "Player 2 won, since player 1 crashed"
                    print("Collision!")
                # Car 2
                offset = (int(car.rect.x - playerCar2.rect.x), int(car.rect.y - playerCar2.rect.y))
                collision_point = player_car2_mask.overlap(coming_cars_masks, offset)
                if collision_point and playerCar2.invincible:
                    # Respawn the car and make it disappear
                    car.changeSpeed(random.randint(50,100))
                    car.repaint()
                    car.rect.y = random.randint(-1000, -100)
                    score_value += 1
                elif collision_point and playerCar2.invisible:
                    # Just go over the car
                    score_value += 1
                elif collision_point:
                    car_crash = True
                    game_over_reason = "Player 1 won, since player 2 crashed"
                    print("Collision!")
            
            
            ''' Pixel perfect collision between players'''
            playerCar1_mask = playerCar1.create_mask()
            playerCar2_mask = playerCar2.create_mask()
            offset = (int(playerCar1.rect.x - playerCar2.rect.x), int(playerCar2.rect.y - playerCar2.rect.y))
            collision_point = playerCar1_mask.overlap(playerCar2_mask, offset)
            if collision_point:
                car_crash = True
                game_over_reason = "The game was tied, since both players crashed"
                print("Collision!")

        
            ''' Pixel perfect collision between player and powerups '''
            if(not pause):  # Player 1
                for powerUp in all_power_ups:
                    powerUpMask = powerUp.create_mask()
                    offset = (int(powerUp.rect.x - playerCar1.rect.x), int(powerUp.rect.y - playerCar1.rect.y))
                    collision_point = player_car_mask.overlap(powerUpMask, offset)
                    if collision_point:
                        
                        # Deactivate the previous power up before activating new one
                        if playerCar1.activePowerUp:
                            playerCar1.activePowerUp.deactivate(playerCar1)
                        
                        # Affect the player
                        powerUp.affectPlayer(playerCar1)
                        powerUp.startTime = pygame.time.get_ticks()
                        playerCar1.activePowerUp = powerUp
                        playerCar1.affected = True
                        
                        # Hide the power up
                        powerUp.rect.y = -9999

            if(not pause):  # Player 2
                for powerUp in all_power_ups:
                    powerUpMask = powerUp.create_mask()
                    offset = (int(powerUp.rect.x - playerCar2.rect.x), int(powerUp.rect.y - playerCar2.rect.y))
                    collision_point = player_car2_mask.overlap(powerUpMask, offset)
                    if collision_point:
                                                
                        # Deactivate the previous power up before activating new one
                        if playerCar2.activePowerUp:
                            playerCar2.activePowerUp.deactivate(playerCar2)
                        
                        # Affect the player
                        powerUp.affectPlayer(playerCar2)
                        powerUp.startTime = pygame.time.get_ticks()
                        playerCar2.activePowerUp = powerUp
                        playerCar2.affected = True
                        
                        # Hide the power up
                        powerUp.rect.y = -9999


            ''' Pixel perfect collision between player and fuel cans '''
            if not pause:  # Player 1
                fuelCanMask = fuel_can.create_mask()
                offset = (int(fuel_can.rect.x - playerCar1.rect.x), int(fuel_can.rect.y - playerCar1.rect.y))
                collision_point = player_car_mask.overlap(fuelCanMask, offset)
                if collision_point:
                    print("Collision with fuel can! (player1)")
                    playerCar1.refuel()
                    is_low_fuel_player1 = False
                    # respawn the fuel can
                    fuel_can.rect.y = random.randint(-2000, -1000)
                    # move to any of the spawn locations different to the current one
                    fuel_can.rect.x = random.choice([loc for loc in powerUpSpawnLocationsX if loc != fuel_can.rect.x])

            if not pause:  # Player 2
                fuelCanMask = fuel_can.create_mask()
                offset = (int(fuel_can.rect.x - playerCar2.rect.x), int(fuel_can.rect.y - playerCar2.rect.y))
                collision_point = player_car2_mask.overlap(fuelCanMask, offset)
                if collision_point:
                    print("Collision with fuel can! (player2)")
                    playerCar2.refuel()
                    is_low_fuel_player2 = False
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
            
            
            ''' Respawn power ups '''
            if(not pause):
                for powerUp in all_power_ups:
                    powerUp.moveForward(main.speed)
                    if powerUp.rect.y > 3*SCREENHEIGHT:  # we are multiplying by 3 to spawn 3 times less powerups than cars
                        powerUp.changeSpeed(random.randint(50, 70))
                        powerUp.repaint() # Repaint to a different power up
                        powerUp.rect.y = random.randint(-1500, -500)
                        powerUp.rect.x = random.choice(powerUpSpawnLocationsX)  # move to any of the spawn locations
     
            
            ''' Respawn fuel cans'''
            if not pause:
                fuel_can.moveForward(main.speed)
                if fuel_can.rect.y > SCREENHEIGHT * 2: # we are multiplying by 2 to spawn 2 times less fuel cans than cars
                    fuel_can.rect.y = random.randint(-300, -50)
                    # move to any of the spawn locations different to the current one
                    fuel_can.rect.x = random.choice([loc for loc in powerUpSpawnLocationsX if loc != fuel_can.rect.x])
            
            
            ''' Display power up timer (player1)'''
            if playerCar1.affected and not pause:
                # Display remaining power up time
                remainingTime = playerCar1.activePowerUp.timeout - (pygame.time.get_ticks() - playerCar1.activePowerUp.startTime)
                if remainingTime > 0:
                    powerUpTimer_background = pygame.image.load("assets/timer_background.png").convert_alpha()
                    powerUpTimer_value = round(remainingTime / 1000, 1)
                    powerUpTimer_font = pygame.font.SysFont('Corbel', 23, bold = True)
                    powerUpTimer_text = powerUpTimer_font.render(str(powerUpTimer_value) + "s", True, (0,0,0))
                    screen.blit(powerUpTimer_background, (0, 120 - (powerUpTimer_background.get_height() // 2)))
                    screen.blit(powerUpTimer_text, ((powerUpTimer_background.get_width() // 2) - (powerUpTimer_text.get_width() // 2), 120 - (powerUpTimer_text.get_height() // 2) + 5))
            
            ''' Display power up timer (player2)'''
            if playerCar2.affected and not pause:
                # Display remaining power up time
                remainingTime = playerCar2.activePowerUp.timeout - (pygame.time.get_ticks() - playerCar2.activePowerUp.startTime)
                if remainingTime > 0:
                    powerUpTimer_background = pygame.image.load("assets/timer_background.png").convert_alpha()
                    powerUpTimer_value = round(remainingTime / 1000, 1)
                    powerUpTimer_font = pygame.font.SysFont('Corbel', 23, bold = True)
                    powerUpTimer_text = powerUpTimer_font.render(str(powerUpTimer_value) + "s", True, (0,0,0))
                    screen.blit(powerUpTimer_background, (SCREENWIDTH - powerUpTimer_background.get_width(), 120 - (powerUpTimer_background.get_height() // 2)))
                    screen.blit(powerUpTimer_text, ((SCREENWIDTH - powerUpTimer_background.get_width()) + (powerUpTimer_background.get_width() // 2) - (powerUpTimer_text.get_width() // 2), 120 - (powerUpTimer_text.get_height() // 2) + 5))
            
            
            ''' Draw the sprites '''
            all_sprites_list.update()
            # Now let's draw all the sprites in one go.
            all_sprites_list.draw(screen)
            
            
            
            ''' Speedometer (player1)'''
            # Defining the position of the speedometer and calculating the angle for the pointer
            speedometer_rect = (20, 460, speedometer.get_rect().x, speedometer.get_rect().y)
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
            
            ''' Speedometer (player2)'''
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



            ''' Gasmeter (player1)'''
            # Update fuel level and ensure doesn't go below 0
            playerCar1.fuel_level -= 0.0005 * main.speed  # make the fuel depend on the speed
            playerCar1.fuel_level = max(playerCar1.fuel_level, 0)

            # Defining the position of the gasmeter and calculating the angle for the pointer
            gasmeter_rect = (20, 320, gasmeter.get_rect().x, gasmeter.get_rect().y)
            gas_angle = -270 * (1 - playerCar1.fuel_level)

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


            ''' Gasmeter (player2)'''
            # Update fuel level and ensure doesn't go below 0
            playerCar2.fuel_level -= 0.0005 * main.speed  # make the fuel depend on the speed
            playerCar2.fuel_level = max(playerCar2.fuel_level, 0)

            # Defining the position of the gasmeter and calculating the angle for the pointer
            gasmeter_rect = (660, 320, gasmeter.get_rect().x, gasmeter.get_rect().y)
            gas_angle = -270 * (1 - playerCar2.fuel_level)

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
            low_fuel_rect_player1 = low_fuel_text.get_rect(center=(80, 300))
            low_fuel_rect_player2 = low_fuel_text.get_rect(center=(720, 300))

            # Update the Low Fuel state
            if playerCar1.fuel_level < low_fuel_threshold:
                is_low_fuel_player1 = True
            else:
                is_low_fuel_player1 = False
                
            if playerCar2.fuel_level < low_fuel_threshold:
                is_low_fuel_player2 = True
            else:
                is_low_fuel_player2 = False

            # Blink Low Fuel message if the state is active
            if is_low_fuel_player1:
                current_time = pygame.time.get_ticks()
                if current_time - last_blink_time > blinking_interval:
                    blink_visible = not blink_visible
                    last_blink_time = current_time

                if blink_visible:
                    screen.blit(low_fuel_text, low_fuel_rect_player1)
                    
            if is_low_fuel_player2:
                current_time = pygame.time.get_ticks()
                if current_time - last_blink_time > blinking_interval:
                    blink_visible = not blink_visible
                    last_blink_time = current_time

                if blink_visible:
                    screen.blit(low_fuel_text, low_fuel_rect_player2)


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
            if(car_crash) or (playerCar1.fuel_level == 0) or (playerCar2.fuel_level == 0):
                # Stop the cars
                main.speed = 0
                
                #pygame.mixer.music.stop()
                
                # Show the Game Over art
                screen.blit(pygame.image.load('assets/game_over.png'), [0, 0, SCREENWIDTH, SCREENHEIGHT])
                
                # Show that player 2 won because player 1 ran out of fuel
                if (playerCar1.fuel_level == 0):
                    gameOverReason_font = pygame.font.SysFont('Corbel', 25, bold = True)
                    gameOverReason_text = gameOverReason_font.render("Player 2 won because player 1 ran out of fuel!", True, WHITE)
                    screen.blit(gameOverReason_text, (SCREENWIDTH//2 - (gameOverReason_text.get_width() // 2), 350))
                
                # Show that player 1 won because player 2 ran out of fuel
                if (playerCar2.fuel_level == 0):
                    gameOverReason_font = pygame.font.SysFont('Corbel', 25, bold = True)
                    gameOverReason_text = gameOverReason_font.render("Player 1 won because player 2 ran out of fuel!", True, WHITE)
                    screen.blit(gameOverReason_text, (SCREENWIDTH//2 - (gameOverReason_text.get_width() // 2), 350))
                    
                # If crash, show the reason and who won
                if (car_crash):
                    gameOverReason_font = pygame.font.SysFont('Corbel', 25, bold = True)
                    gameOverReason_text = gameOverReason_font.render(game_over_reason, True, WHITE)
                    screen.blit(gameOverReason_text, (SCREENWIDTH//2 - (gameOverReason_text.get_width() // 2), 350))
                
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
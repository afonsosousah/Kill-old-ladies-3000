import pygame, random
import game
import main

WHITE = (255, 255, 255)

class Car(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, width, height, speed, model, flip=True):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        #self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(f"assets/car{model}.png").convert_alpha()
        if flip:
            self.image = pygame.transform.flip(self.image, True, True)
        self.original_image = self.image

        #Initialise attributes of the car.
        self.width = width
        self.height = height
        self.speed = speed
        self.side_speed = 0
        self.flip = flip
        self.model = model
        self.fuel_level = 1.0
        
        # Power up atributes
        self.invincible = False
        self.slowing = False
        self.invisible = False
        self.affected = False
        self.activePowerUp = None

        # Draw the car (a rectangle!)
            #pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        

        # Instead we could load a proper picture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        new_speed = self.side_speed + (pixels / 20)
        if new_speed <= 7 and new_speed >= -7:
            self.side_speed = new_speed
        if not self.collide(main.MAP_BORDER_MASK, -self.side_speed):
            self.rect.x += self.side_speed
        else:
            self.bounce()

    def moveLeft(self, pixels):
        new_speed = self.side_speed - (pixels / 20)
        if new_speed <= 7 and new_speed >= -7:
            self.side_speed = new_speed
        if not self.collide(main.MAP_BORDER_MASK, -self.side_speed):
            self.rect.x += self.side_speed
        else:
            self.bounce()

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, isPlayer=False):
        models = [1, 2, 3, 4, 5, 6]
        if not isPlayer:
            # Remove the player's car model from the list of all coming car potential models
            if main.selected_car in models:
                models.remove(main.selected_car)
        
        # Remove the current model to ensure the car is repainted to a different model
        if self.model in models:
            models.remove(self.model)
    
        # Choose a new model from the remaining models
        new_model = random.choice(models)

        # Load the new car image and apply flip if necessary
        self.image = pygame.image.load(f"assets/car{new_model}.png").convert_alpha()
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, True)
    
        # Update the car's model attribute to the new model
        self.model = new_model
        
    # Is used to repaint the player car back to default when repaint powerup ends
    def repaintOriginal(self):
        # The new model is the original one
        new_model = main.selected_car

        # Load the new car image and apply flip if necessary
        self.image = pygame.image.load(f"assets/car{new_model}.png").convert_alpha()
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, True)
    
        # Update the car's model attribute to the new model
        self.model = new_model

    def setInvisible(self):
        # Make the car not collide
        self.invisible = True
        # Save the original image of the car to restore it later
        self.original_image = self.image
        # Load the "ghost" version of the car
        self.image = pygame.image.load(f'assets/ghostcar{main.selected_car}.png').convert_alpha()
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, True)

    def setVisible(self):
        # Make the car collide again
        self.invisible = False
        # Restore the original image of the car
        self.image = self.original_image
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, True)

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.image)
        offset = (int(self.rect.x - x), int(self.rect.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi
    
    def bounce(self):
        # make the car slower
        self.speed -= 0.05
        if self.rect.x < 800/2:
            # car hit the left border
            self.side_speed += 10
            self.rect.x += self.side_speed
        else:
            # car hit the right border
            self.side_speed -= 10
            self.rect.x += self.side_speed
    
    def create_mask(self):
        return pygame.mask.from_surface(self.image)

    def refuel(self):
        self.fuel_level += 0.5
        self.fuel_level = min(self.fuel_level, 1.0) # Prevent overfilling



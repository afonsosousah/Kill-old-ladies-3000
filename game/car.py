import pygame, random
import main

WHITE = (255, 255, 255)

class Car(pygame.sprite.Sprite):
    """
    Car Class

    This class represents a car in the Turbo Racing 3000 game.
    It derives from the Sprite class from pygame.
    It handles aspects like movement, collision detection, power-ups, and fuel level.

    Attributes:
    ----------
    width: int
        Width of the car image.
    height: int
        Height of the car image.
    speed: int
        The speed at which the car moves along the track.
    side_speed: int
        The horizontal speed of the car, controlling its movement left and right.
    flip: bool
        Whether the car should be flipped horizontally (for right-handed/left-handed mode).
    model: int
        Index of the car model, ranging from 1 to 6.
    fuel_level: float
        Current fuel level of the car, ranging from 0.0 to 1.0.

    Methods:
    -------
    moveRight(pixels):
        Moves the car to the right by the specified number of pixels.
    moveLeft(pixels):
        Moves the car to the left by the specified number of pixels.
    moveForward(speed):
        Moves the car forward along the track by the specified speed.
    moveBackward(speed):
        Moves the car backward along the track by the specified speed.
    changeSpeed(speed):
        Changes the car's overall movement speed to the specified value.
    repaint(isPlayer=False):
        Repaints the car's image to a random model, except for the player's car.
    repaintOriginal(player):
        Repaints the player's car back to its original model after the repaint powerup ends.
    setInvisible():
        Makes the car invisible and loads a ghost image.
    setVisible():
        Makes the car visible again and loads its original image.
    collide(mask, x=0, y=0):
        Checks for collision between the car and the specified mask.
    bounce():
        Handles bouncing off the track boundaries.
    create_mask():
        Returns a Pygame mask object for collision detection.
    refuel():
        Increases the car's fuel level by 0.5, up to a maximum of 1.0.

    """

    def __init__(self, width, height, speed, model, flip=True):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set the image of the car
        self.image = pygame.image.load(f"assets/car{model}.png").convert_alpha()
        if flip:
            self.image = pygame.transform.flip(self.image, True, True)
        

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
        self.original_speed = speed
        self.original_image = self.image
        self.original_model = model

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
        
    def moveForwardPlayer(self):
        self.rect.y -= self.speed // 50
        
    def moveBackwardPlayer(self):
        self.rect.y += self.speed // 50

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, isPlayer=False):
        models = [1, 2, 3, 4, 5, 6]
        
        if not main.selected_car2: # If its not multiplayer
            # Remove the player's car model from the list of all coming car potential models
            models.remove(main.selected_car)
        else: # The game is in multiplayer
            models.remove(main.selected_car)
            models.remove(main.selected_car2)
        
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
    def repaintOriginal(self, player):
        # The new model is the original one
        new_model = player.original_model

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
        self.image = pygame.image.load(f'assets/ghostcar{self.original_model}.png').convert_alpha()
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



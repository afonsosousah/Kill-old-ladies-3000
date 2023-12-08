import pygame

class FuelCan(pygame.sprite.Sprite):
    """
    Fuel Can Class

    This class represents a Fuel Can in the Turbo Racing 3000 game.
    It derives from the Sprite class from pygame.
    The fuel can is an object that the player can collect to replenish their car's fuel. 
    When the player collides with a fuel can, their car's fuel level increases, allowing them to race for a longer duration.

    Attributes:
    ----------
    speed: int
        The speed at which the Fuel Can moves along the track.

    Methods:
    -------
    moveForward(speed):
        Moves the Fuel Can forward by the specified speed.
    moveBackward(speed):
        Moves the Fuel Can backward by the specified speed.
    changeSpeed(speed):
        Changes the Fuel Can's movement speed to the specified value.
    create_mask():
        Returns a Pygame mask object for collision detection.
    """
    
    def __init__(self, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Set the fuel can image
        self.image = pygame.image.load(f'assets/fuel_can.png')

        #Initialise attributes of the sprite.
        self.width = 50
        self.height = 50
        self.speed = speed

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveForward(self, speed):
        self.rect.y += speed * 2

    def moveBackward(self, speed):
        self.rect.y -= speed * 2

    def changeSpeed(self, speed):
        self.speed = speed
    
    def create_mask(self):
        return pygame.mask.from_surface(self.image)
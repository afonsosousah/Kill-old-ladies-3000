import pygame, random

class Map(pygame.sprite.Sprite):
    # This class represents the map. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.image.load("assets/infinite_level.png").convert_alpha()
        #self.image.set_colorkey(WHITE)

        # Initialise attributes of the map.
        self.width = width
        self.height = height
        self.speed = speed

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveDown(self, speed):
        self.rect.y += self.speed * speed / 12.5

    def moveUp(self, speed):
        self.rect.y -= self.speed * speed / 12.5

    def changeSpeed(self, speed):
        self.speed = speed
    
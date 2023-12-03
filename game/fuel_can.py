import random
import pygame
import main

class FuelCan(pygame.sprite.Sprite):
    # This class represents a Fuel Can
    # A player can “catch” a Fuel Can by hitting it with the car. 
    # Catching a “Fuel Can” will add fuel to the car, allowing the user to play for more time.
    
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
import random
import pygame
import main

WHITE = (255, 255, 255)

powerUpKeys = {}

class Power_Up(pygame.sprite.Sprite):
    # This class represents a Power-Up
    # A Power-Up something a player can “catch” by hitting it with the car. 
    # Catching a “Power-up” will affect the game in some way for a temporary amount of time.
    
    # The available types of power-ups are: Invincibility, Slowing, Repaint and Random
    def __init__(self, type, speed, timeout = 3000):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        #self.image = pygame.Surface([50, 50])
        #self.image.fill(WHITE)
        #self.image.set_colorkey(WHITE)
        self.image = pygame.image.load(f'assets/powerup_{type}.png')

        #Initialise attributes of the car.
        self.width = 50
        self.height = 50
        self.speed = speed
        self.type = type
        
        self.startTime = None  # property to use for the timeout of the powerup
        self.timeout = timeout  # 3 seconds timeout default
        self.typeWhenActivated = None  # store what was the type when the power up was last activated
        # we need to do this because the powerup will be reused after colliding with the player
        # and its type can change

        # Draw the car (a rectangle!)
        #pygame.draw.circle(self.image, self.color, [self.width/2, self.height/2], self.width/2)

        # Instead we could load a proper picture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def affectPlayer(self, player):
        powerUpTypes = ("invincibility", "slowing", "repaint", "invisibility")
        
        if self.type == "random":
            self.type = random.choice(powerUpTypes)
        
        if self.type == "invincibility":
            # To be defined
            player.bounce()
        elif self.type == "slowing":
            main.speed = 0.2
        elif self.type == "repaint":
            player.repaint()

        elif self.type == "invisibility":
            # To be defined
            player.invisible()
        
        main.active_power_up = self
        self.startTime = pygame.time.get_ticks()
        self.typeWhenActivated = self.type
    
    def deactivate(self):
        print("deactivate power up")
        
        if self.typeWhenActivated == "invincibility":
            # To be defined
            pass
        elif self.typeWhenActivated == "slowing":
            main.speed = 1
        elif self.typeWhenActivated == "repaint":
            pass
        elif self.typeWhenActivated == "invisibility":
            pass
        
        main.active_power_up = None
        self.startTime = None
        self.typeWhenActivated = None

    def moveForward(self, speed):
        self.rect.y += speed * 2

    def moveBackward(self, speed):
        self.rect.y -= speed * 2

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, type):
        self.image = pygame.image.load(f'assets/powerup_{type}.png')
        self.type = type

    def invisible(self, type):
        self.image = pygame.image.load(f'assets/powerup_{type}.png')
        self.type = type
    
    def create_mask(self):
        return pygame.mask.from_surface(self.image)
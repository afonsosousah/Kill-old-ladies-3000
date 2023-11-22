import pygame
WHITE = (255, 255, 255)

class Power_Up(pygame.sprite.Sprite):
    # This class represents a Power-Up
    # A Power-Up something a player can “catch” by hitting it with the car. 
    # Catching a “Power-up” will affect the game in some way for a temporary amount of time.
    
    # The available types of power-ups are: Test, Invincibility, Slowing
    def __init__(self, type, color, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([50, 50])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #Initialise attributes of the car.
        self.width = 50
        self.height = 50
        self.color = color
        self.speed = speed

        # Draw the car (a rectangle!)
        pygame.draw.circle(self.image, self.color, [self.width/2, self.height/2], self.width/2)

        # Instead we could load a proper picture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self, color):
        self.color = color
        pygame.draw.circle(self.image, self.color, [self.width/2, self.height/2], self.width/2)
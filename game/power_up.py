import random
import pygame
import main

WHITE = (255, 255, 255)

powerUpKeys = {}

class PowerUp(pygame.sprite.Sprite):
    # This class represents a Power-Up
    # A Power-Up is something a player can “catch” by hitting it with the car. 
    # Catching a “Power-up” will affect the game in some way for a temporary amount of time.
    
    # The available types of power-ups are: Invincibility, Slowing, Repaint, Invisibility and Random
    def __init__(self, speed, timeout = 3000):
        # Call the parent class (Sprite) constructor
        super().__init__()

        #Initialise attributes of the sprite.
        self.width = 50
        self.height = 50
        self.speed = speed
        #self.type = type
        
        self.startTime = None  # property to use for the timeout of the powerup
        self.timeout = timeout  # 3 seconds timeout default
        #self.typeWhenActivated = None  # store what was the type when the power up was last activated
        # we need to do this because the powerup will be reused after colliding with the player
        # and its type can change
    
    # Function that is called when the player catches a power up
    def affectPlayer(self, player):
        pass
        
    # Function that is called when the player catches a power up
    def deactivate(self, player): 
        self.repaint()
        player.affected = False
        player.activePowerUp = None

    def moveForward(self, speed):
        self.rect.y += speed * 2

    def moveBackward(self, speed):
        self.rect.y -= speed * 2

    def changeSpeed(self, speed):
        self.speed = speed

    def repaint(self):
        # Define where the power ups spawn
        powerUpSpawnLocationsX = (250, 390, 500)  # spawn in the middle of the lanes
        
        # Define the types and weights
        powerUpTypes = [Invincibility, Slowing, Repaint, Invisibility]
        powerUpWeights = [15, 25, 20, 10]
        
        # Remove the current power up class from the list
        index = powerUpTypes.index(self.__class__)
        powerUpTypes.pop(index)
        powerUpWeights.pop(index)
        
        # Set the new class  of power up
        self.__class__ = random.choices(powerUpTypes, powerUpWeights)[0]
        
        self.__init__(random.randint(50, 70))
        
        # Move to new location
        self.rect.y = random.randint(-5000, -1000)
        self.rect.x = random.choice(powerUpSpawnLocationsX)  # move to any of the spawn locations
    
    
    def create_mask(self):
        return pygame.mask.from_surface(self.image)


class Invincibility(PowerUp):
    
    def __init__(self, speed, timeout=3000):
        super().__init__(speed, timeout)
        
        # Set the power up image
        self.image = pygame.image.load(f'assets/powerup_invincibility.png')
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def affectPlayer(self, player):        
        # Make the changes to the player
        player.invincible = True
        player.image = pygame.image.load(f'assets/car_invincible.png')
        pygame.time.set_timer(pygame.USEREVENT, 3000, 1)
    
    def deactivate(self, player):
        super().deactivate(player)  # Repaint the power up
        player.invincible = False
        player.image = pygame.image.load(f'assets/car{main.selected_car}.png')
        

class Slowing(PowerUp):
    
    def __init__(self, speed, timeout=3000):
        super().__init__(speed, timeout)
        self.original_speed = 1
        
        # Set the power up image
        self.image = pygame.image.load(f'assets/powerup_slowing.png')
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def affectPlayer(self, player):
        self.original_speed = main.speed
        main.speed = 0.2
        player.slowing = True
        player.image = pygame.image.load(f'assets/car_slowing.png')
        pygame.time.set_timer(pygame.USEREVENT, 3000, 1)
    
    def deactivate(self, player):
        super().deactivate(player)
        main.speed = self.original_speed
        player.slowing = False
        player.image = pygame.image.load(f'assets/car{main.selected_car}.png')
        
        
class Repaint(PowerUp):
    
    def __init__(self, speed, timeout=3000):
        super().__init__(speed, timeout)
        
        # Set the power up image
        self.image = pygame.image.load(f'assets/powerup_repaint.png')
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def affectPlayer(self, player):
        player.repaint(isPlayer=True)
        pygame.time.set_timer(pygame.USEREVENT, 3000, 1)
    
    def deactivate(self, player):
        super().deactivate(player)
        player.repaintOriginal()
    

class Invisibility(PowerUp):
    
    def __init__(self, speed, timeout=3000):
        super().__init__(speed, timeout)
        
        # Set the power up image
        self.image = pygame.image.load(f'assets/powerup_invisibility.png')
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def affectPlayer(self, player):
        player.setInvisible()
        pygame.time.set_timer(pygame.USEREVENT, 3000, 1)
    
    def deactivate(self, player):
        super().deactivate(player)
        player.setVisible()
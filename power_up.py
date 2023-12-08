import random
import pygame
import main

WHITE = (255, 255, 255)

powerUpKeys = {}

class PowerUp(pygame.sprite.Sprite):
    """
    Power-Up Class

    This class represents a Power-Up object in the Turbo Racing 3000 game.
    It derives from the Sprite class from pygame.
    A Power-Up is a collectible item that players can collect by colliding with it.
    Different types of power-ups have varying effects on the game, 
    such as increasing player speed, reducing enemy speed, or making the player temporarily invincible.

    Attributes:
    ----------
    width: int
        The width of the Power-Up sprite.
    height: int
        The height of the Power-Up sprite.
    speed: int
        The speed at which the Power-Up moves along the track.
    startTime: float
        Timestamp of when the Power-Up was activated.
    timeout: int
        Duration for which the Power-Up's effects last.

    Methods:
    -------
    affectPlayer(player):
        Applies the Power-Up's effect to the specified player.
    deactivate(player):
        Removes the Power-Up's effect from the specified player.
    moveForward(speed):
        Moves the Power-Up forward by the specified speed.
    moveBackward(speed):
        Moves the Power-Up backward by the specified speed.
    changeSpeed(speed):
        Changes the Power-Up's movement speed to the specified value.
    repaint():
        Creates a new Power-Up object with a random type and respawns it.
    create_mask():
        Returns a Pygame mask object for collision detection.

    """
    
    
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
        powerUpTypes = [Invincibility, Slowing, Repaint, Invisibility, Random]
        powerUpWeights = [15, 25, 20, 10, 30]
        
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
    """
    Invincibility Power-Up Class

    This child class of the `PowerUp` class represents the invincibility power-up in the Turbo Racing 3000 game.

    The invincibility power-up makes the player car invulnerable to collisions with other cars or obstacles for a short duration.

    Attributes:
    ----------
    speed: int
        The speed at which the Power-Up moves along the track.
    timeout: int
        Duration for which the Power-Up's effects last.

    Methods:
    -------
    affectPlayer(player):
        Applies the invincibility effect to the specified player.
    deactivate(player):
        Removes the invincibility effect from the specified player.

    """
    
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
        player.image = pygame.image.load(f'assets/car{player.original_model}.png')


class Slowing(PowerUp):
    """
    Slowing Power-Up Class

    This child class of the `PowerUp` class represents the slowing power-up in the Turbo Racing 3000 game.
    It slows down all cars, including the player's car, for a brief period.

    Attributes:
    ----------
    speed: int
        The speed at which the Power-Up moves along the track.
    timeout: int
        Duration for which the Power-Up's effects last.

    Methods:
    -------
    affectPlayer(player):
        Slows down all cars.
    deactivate(player):
        Reverts all cars' speed and image to original state.

    """

    def __init__(self, speed, timeout=3000):
        super().__init__(speed, timeout)
        self.original_speed = 1
        
        # Set the power up image
        self.image = pygame.image.load(f'assets/powerup_slowing.png')
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def affectPlayer(self, player):
        for car in main.all_coming_cars:
            car.original_speed = car.speed
            car.speed *= 0.4
            car.original_image = car.image
            car.image = pygame.image.load(f'assets/car_slowing.png')

        pygame.time.set_timer(pygame.USEREVENT, 3000, 1)
    
    def deactivate(self, player):
        super().deactivate(player)

        for car in main.all_coming_cars:
            car.speed = car.original_speed
            car.image = car.original_image
        
        
class Repaint(PowerUp):
    """
    Repaint Power-Up Class

    This child class of the `PowerUp` class represents the repaint power-up in the Turbo Racing 3000 game.
    The repaint power-up changes the appearance of all the cars on the track, including the player's car, for a short duration.

    Attributes:
    ----------
    speed: int
        The speed at which the Power-Up moves along the track.
    timeout: int
        Duration for which the Power-Up's effects last.

    Methods:
    -------
    affectPlayer(player):
        Changes the appearance of all cars.
    deactivate(player):
        Reverts all cars' appearance to original state.

    """
    
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
        player.repaintOriginal(player)
    

class Invisibility(PowerUp):
    """
    Invisibility Power-Up Class

    This child class of the `PowerUp` class represents the invisibility power-up in the Turbo Racing 3000 game.
    The invisibility power-up makes the player car temporarily invisible to other cars and obstacles, making it harder to be hit.

    Attributes:
    ----------
    speed: int
        The speed at which the Power-Up moves along the track.
    timeout: int
        Duration for which the Power-Up's effects last.

    Methods:
    -------
    affectPlayer(player):
        Makes the player car invisible.
    deactivate(player):
        Reveals the player car.

    """
    
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


class Random(PowerUp):
    """
    Random Power-Up Class

    This child class of the `PowerUp` class represents the random power-up in the Turbo Racing 3000 game.
    It randomly activates one of the four other power-ups (Invincibility, Slowing, Repaint, Invisibility) and applies its effect to the player car.

    Attributes:
    ----------
    speed: int
        The speed at which the Power-Up moves along the track.
    timeout: int
        Duration for which the Power-Up's effects last.

    Methods:
    -------
    affectPlayer(player):
        Randomly activates one of the four power-ups and applies its effect.
    deactivate(player):
        Reverts the applied effect and clears the active power-up from the player object.

    """

    def __init__(self, speed, timeout=3000):
        super().__init__(speed, timeout)
        
        # Set the power up image
        self.image = pygame.image.load(f'assets/powerup_random.png')
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()


    def affectPlayer(self, player):

        # Randomly activate one of the power-ups
        available_powerups = [Invincibility, Slowing, Repaint, Invisibility]
        chosen_powerup_class = random.choice(available_powerups)
        chosen_powerup = chosen_powerup_class(self.speed, self.timeout)
        chosen_powerup.affectPlayer(player)

        pygame.time.set_timer(pygame.USEREVENT, 3000, 1)

        # Store the active power-up in the player object for later deactivation
        player.active_powerup = chosen_powerup


    def deactivate(self, player):
        # Ensure there's an active power-up to deactivate
        if player.active_powerup:
            # Deactivate the currently active power-up
            player.active_powerup.deactivate(player)
            
            # Clear the active power-up after deactivation
            player.active_powerup = None
            
            # Restore the player's car image to its original state
            player.image = pygame.image.load(f'assets/car{player.original_model}.png').convert_alpha()


import pygame, random
import game
import main

WHITE = (255, 255, 255)

class Car(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height, speed, model, flip=True):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        #self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(f"assets/car{model}.png").convert_alpha()
        if flip:
            self.image = pygame.transform.flip(self.image, True, True)
        #self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #Initialise attributes of the car.
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.side_speed = 0
        self.flip = flip
        self.model = model
        
        # Power up atributes
        self.invincible = False

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
        if not self.collide(game.MAP_BORDER_MASK, -self.side_speed):
            self.rect.x += self.side_speed
        else:
            self.bounce()

    def moveLeft(self, pixels):
        new_speed = self.side_speed - (pixels / 20)
        if new_speed <= 7 and new_speed >= -7:
            self.side_speed = new_speed
        if not self.collide(game.MAP_BORDER_MASK, -self.side_speed):
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
        models = [1,2,3,4,5,6]
        models.remove(self.model)
        new_model = random.choice(models) # repaint to a different car
        
        if isPlayer:
            main.selected_car = new_model
        
        self.image = pygame.image.load(f"assets/car{new_model}.png").convert_alpha()
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, True)

    def invisible(self):
        # Make the car not collide
        self.invincible = True
        # Save the original image of the car to restore it later
        self.original_image = self.image
        # Load the "ghost" version of the car
        self.image = pygame.image.load(f'assets/ghostcar{main.selected_car}.png').convert_alpha()
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, True)

    def visible(self):
        # Make the car collide again
        self.invincible = False
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



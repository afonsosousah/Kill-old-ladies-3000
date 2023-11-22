import pygame, random
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
        self.flip = flip

        # Draw the car (a rectangle!)
            #pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        

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

    def repaint(self):
        self.image = pygame.image.load(f"assets/car{random.randint(1,6)}.png").convert_alpha()
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, True)

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.image)
        offset = (int(self.rect.x - x), int(self.rect.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi
    
    def bounce(self):
        self.speed -= 0.05
        if self.rect.x < 800/2:
            # car hit the left border
            self.moveRight(20)
        else:
            # car hit the right border
            self.moveLeft(20) 

    def create_mask(self):
        return pygame.mask.from_surface(self.image)



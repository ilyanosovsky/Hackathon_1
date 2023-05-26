import pygame

class Ino(pygame.sprite.Sprite): # create a child class of Sprite
    # class of Ino

    def __init__(self, screen):
        # initialize the Ino and set its starting position
        super(Ino, self).__init__() # initialize the parent class of Ino
        self.screen = screen # assign screen to the Ino class
        self.image = pygame.image.load('SpaceGame/image/ino.png') # load image of Ino
        self.image = pygame.transform.scale(self.image, (50, 50)) # scale image of Ino
        self.rect = self.image.get_rect() # get rectangle of Ino
        self.rect.x = self.rect.width # set x coordinate of Ino to the width of the rectangle
        self.rect.y = self.rect.height # set y coordinate of Ino to the height of the rectangle
        self.x = float(self.rect.x) # set x coordinate of Ino to the float of the x coordinate of the rectangle
        self.y = float(self.rect.y) # set y coordinate of Ino to the float of the y coordinate of the rectangle

    def draw(self): 
        # draw Ino at the current position
        self.screen.blit(self.image, self.rect) 

    def update(self): 
        # move Inos 
        self.y += 0.1 # move Ino down
        self.rect.y = self.y # set y coordinate of Ino to the y coordinate of the rectangle

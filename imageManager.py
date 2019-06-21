import pygame
from pygame.locals import *

class Photo:
     
    def __init__(self, filePath):
        self.image = pygame.image.load(filePath)
        # Save scaled version of image
        self.scaledImage = self.image
        # Save the initial width and height ratio
        (self.width, self.height) = self.image.get_size()
        print(self.image.get_size())
        self.xpos = 0
        self.ypos = 0

    def draw(self, screen):
        screen.blit(self.scaledImage, (self.xpos, self.ypos))

    def resize(self, newWidth, newHeight):
        self.scaledImage = pygame.transform.scale(self.image, (newWidth, newHeight))

    
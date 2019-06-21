import pygame
from pygame.locals import *

class Photo:
     
    def __init__(self, filePath):
        self.image = pygame.image.load(filePath)
        self.xpos = 0
        self.ypos = 0

    def draw(self, screen):
        screen.blit(self.image, (self.xpos, self.ypos))

    def resize(self, newWidth, newHeight):
        self.image = pygame.transform.scale(self.image, (newWidth, newHeight))

    
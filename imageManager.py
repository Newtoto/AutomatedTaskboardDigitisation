import pygame
from pygame.locals import *

import re

class Photo:     

    # File path is written like "./Images/2019-02-28/taskboardImage_12-58-25.jpg"
    appendedString = "taskboardImage_"


    def __init__(self, filePath):
        self.image = pygame.image.load(filePath)
        # Save scaled version of image
        self.scaledImage = self.image
        # Save the initial width and height ratio
        (self.width, self.height) = self.image.get_size()
        print(self.image.get_size())
        self.xpos = 0
        self.ypos = 0
        # # Split up file name from directories
        # processText = filePath.split("/")
        # # Get date value from 2nd directory
        # self.dateText = processText[1]
        # # Remove appended string from before file name
        # processText = processText[2].split
        
        # processText = processText[1]
        # processText = processText.split("_")
        # self.timeText = processText[1]

        self.dateText = re.search("Images/(.*)/", filePath).group(1)
        self.timeText = re.search("taskboardImage_(.*).jpg", filePath).group(1)
        print(self.dateText)
        print(self.timeText)

    
    def draw(self, screen):
        screen.blit(self.scaledImage, (self.xpos, self.ypos))

    def resize(self, newWidth, newHeight):
        self.scaledImage = pygame.transform.scale(self.image, (newWidth, newHeight))

    
import pygame
from pygame.locals import *

import re
import math

class Photo:     

    # File path is written like "./Images/2019-02-28/taskboardImage_12-58-25.jpg"

    def __init__(self, filePath):
        self.image = pygame.image.load(filePath)
        # Save scaled version of image
        self.scaledImage = self.image
        # Save the initial width and height ratio
        (self.width, self.height) = self.image.get_size()
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

    
    def draw(self, screen):
        screen.blit(self.scaledImage, (self.xpos, self.ypos))

    def resize(self, screen_width, screen_height):
        # width = ratio * height
        # If this is lower, width determines maximum size
        screen_ratio = screen_width/screen_height
        print(screen_ratio)
        # If this is lower, height determines maximum size
        image_ratio = self.width/self.height
        print(image_ratio)

        # Set height and width
        (scaled_height, scaled_width) = (screen_height, screen_width)

        if screen_ratio < image_ratio:
            # Set width and calculate height
            scaled_width = screen_width
            scaled_height = screen_width / image_ratio
        elif image_ratio < screen_ratio:
            # Set height and calculate width
            scaled_height = screen_height
            scaled_width = screen_height * image_ratio

        # Turn scaled values into integers
        scaled_height = math.floor(scaled_height)
        scaled_width = math.floor(scaled_width)

        # Offset postions to center image
        self.xpos = (screen_width - scaled_width)/2
        self.ypos = (screen_height - scaled_height)/2

        # Create scaled image
        self.scaledImage = pygame.transform.scale(self.image, (scaled_width, scaled_height))

    
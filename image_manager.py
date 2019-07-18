'''Contains Photo class'''
from __future__ import division
import pygame
from pygame.locals import *

import re
import math

class Photo:     
    '''Controls the drawing, scaling and placement of an image taken from an image file'''
    # File path is this format: "./Images/taskboardImage_date_time.jpg"

    def __init__(self, filePath):
        self.image = pygame.image.load(filePath)
        # Save scaled version of image
        self.scaled_image = self.image
        # Save the initial width and height ratio
        (self.width, self.height) = self.image.get_size()
        self.xpos = 0
        self.ypos = 0
        # Get date and time from file path
        dateAndTimeText = re.search("Images/taskboardImage_(.*).jpg", filePath).group(1)
        self.date_text = dateAndTimeText.split("_")[0]
        self.time_text = dateAndTimeText.split("_")[1]
        self.ordering_value = int((self.date_text + self.time_text).replace("-",""))

    def draw(self, screen, font, area_width, area_height):
        '''Draws scaled image and info text onto screen'''
        # Scale image
        self.resize(area_width, area_height)
        # Show image
        screen.blit(self.scaled_image, (self.xpos, self.ypos))
        # Write text
        date_text = font.render(self.date_text, False, (0, 0, 0))
        time_text = font.render(self.time_text, False, (0, 0, 0))
        screen.blit(date_text, (0, 0))
        screen.blit(time_text, (0, 30))

    def resize(self, area_width, area_height):
        '''Scales the image and centers within area'''
        # width = ratio * height
        # If this is lower, width determines maximum size
        screen_ratio = area_width/area_height
        # If this is lower, height determines maximum size
        image_ratio = self.width/self.height

        # Set height and width
        (scaled_height, scaled_width) = (area_height, area_width)
        
        if screen_ratio < image_ratio:
            # Set width and calculate height
            scaled_width = area_width
            scaled_height = area_width / image_ratio
        elif image_ratio < screen_ratio:
            # Set height and calculate width
            scaled_height = area_height
            scaled_width = area_height * image_ratio
        
        # Turn scaled values into integers
        scaled_height = int(math.floor(scaled_height))
        scaled_width = int(math.floor(scaled_width))

        # Offset postions to center image
        self.xpos = (area_width - scaled_width)/2
        self.ypos = (area_height - scaled_height)/2

        # Create scaled image
        self.scaled_image = pygame.transform.scale(self.image, (scaled_width, scaled_height))

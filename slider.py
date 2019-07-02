'''All classes which pertain to the slider control at the bottom of the page'''
from __future__ import division
import math
import pygame

class SliderContainer:
    '''Contains all parts of the slider'''
    def __init__(self, screen, height_percentage, images):
        self.height_percentage = height_percentage
        self.slider = Slider(images)
        # Initialise position and size variables
        self.width, self.height, self.xpos, self.ypos = (0, 0, 0, 0)
        self.resize(screen)

    def draw(self, screen):
        '''Draws all parts of resized slider'''
        pygame.draw.rect(screen, (0, 0, 0), ((0, self.ypos), (self.width, self.height)))
        # Draw slider segments and slider
        self.slider.draw_slider(screen)

    def resize(self, screen):
        '''Scales slider to portion of screen'''
        # Scale slider background
        # Get height and width from screen
        self.width, self.height = screen.get_size()
        # Calculate y offset to be 90% of screen
        self.ypos = self.height * (1 - self.height_percentage)
        # Adjust height
        self.height = self.height * self.height_percentage
        # Scale slider segments
        self.slider.calculate_size(self)

class Slider:
    '''Segments and slider object inside the slider container'''
    def __init__(self, images):
        self.segment_quantity = len(images)
        # With is 90% of container width
        self.relative_width = 0.95
        # Height is 50% of container height
        self.relative_height = 0.5
        # Initialise position and size variables
        self.dragger_xpos_percent = 0
        self.rect = pygame.Rect((0, 0), (0, 0))
        self.dragger_width = 10
        self.current_image = 0

    def draw_segments(self, screen):
        '''Draws sement for each image in array'''
        # Calculate width of each segment
        segment_width = self.rect.width / self.segment_quantity
        for x in range(0, self.segment_quantity):
            # Alternate segment colour
            if x % 2 == 0:
                colour_value = 30 
            else:
                colour_value = 90
            # Uncomment below for debugging (doesn't work for lots of segments)
            # colour_value = 50 * x + 40
            segment_colour = (colour_value, colour_value, colour_value)
            xpos = ((self.rect.width / self.segment_quantity) * x) + self.rect.left
            rect = ((xpos, self.rect.top), (segment_width, self.rect.height))
            pygame.draw.rect(screen, segment_colour, rect)

    def calculate_size(self, slider_container):
        '''Works out size and positioning using slider container'''
        # Calculate width
        self.rect.width = (slider_container.width) * self.relative_width
        # Calculate height
        self.rect.height = slider_container.height * self.relative_height

        # position is half the difference with container plus the position of the container
        self.rect.left = ((slider_container.width - self.rect.width) / 2) + slider_container.xpos
        self.rect.top = ((slider_container.height - self.rect.height) / 2) + slider_container.ypos

    def draw_draggable_object(self, screen):
        '''Draws object which you drag to select the image'''
        rect = ((int(self.dragger_xpos_percent * self.rect.width) + self.rect.left, self.rect.top), (self.dragger_width, self.rect.height))
        pygame.draw.rect(screen, (255, 255, 255), rect)

    def drag(self, mouse_pos):
        '''Changes position of slider to mouse if in collision area'''
        print mouse_pos
        # Check mouse is in range of clicking
        if self.rect.collidepoint(mouse_pos):
            self.dragger_xpos_percent = (mouse_pos[0] - (self.dragger_width / 2) - self.rect.left) / self.rect.width
            # Update image
            self.calculate_image()

    def draw_slider(self, screen):
        '''Draws segments and then slider over the top'''
        self.draw_segments(screen)
        self.draw_draggable_object(screen)
        pygame.display.update()

    def calculate_image(self):
        '''Gives image closest to slider position'''
        print(self.segment_quantity * self.dragger_xpos_percent)
        return int(math.floor(self.segment_quantity * self.dragger_xpos_percent))

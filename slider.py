'''All classes which pertain to the slider control at the bottom of the page'''
import math
import pygame

class SliderContainer:
    '''Contains all parts of the slider'''
    def __init__(self, screen, height_percentage, images):
        self.height_percentage = height_percentage
        self.resize(screen)
        self.slider = Slider(images)
        # Initialise position and size variables
        self.width, self.height, self.xpos, self.ypos = (0, 0, 0, 0)

    def draw(self, screen):
        '''Draws all parts of resized slider'''
        self.resize(screen)
        pygame.draw.rect(screen, (0, 0, 0), ((0, self.ypos), (self.width, self.height)))
        # Resize slider segments
        self.slider.calculate_size(self)
        # Draw segments over container
        self.slider.draw_segments(screen)

    def resize(self, screen):
        '''Scales slider to portion of screen'''
        # Get height and width from screen
        self.width, self.height = screen.get_size()
        # Calculate y offset to be 90% of screen
        self.ypos = self.height * (1 - self.height_percentage)
        # Adjust height
        self.height = self.height * self.height_percentage

class Slider:
    '''Segments and slider object inside the slider container'''
    def __init__(self, images):
        self.segment_quantity = len(images)
        # With is 90% of container width
        self.relative_width = 0.95
        # Height is 50% of container height
        self.relative_height = 0.5
        # Initialise position and size variables
        self.width, self.height, self.xpos, self.ypos = (0, 0, 0, 0)

    def draw_segments(self, screen):
        '''Draws sement for each image in array'''
        # Calculate width of each segment
        segment_width = self.width / self.segment_quantity
        for x in range(0, self.segment_quantity):
            # Colour of segment
            colour_value = 30
            # Uncomment below for debugging (doesn't work for lots of segments)
            # colour_value = 50 * x + 40
            segment_colour = (colour_value, colour_value, colour_value)
            xpos = ((self.width / self.segment_quantity) * x) + self.xpos
            rect = ((xpos, self.ypos), (segment_width, self.height))
            
            pygame.draw.rect(screen, segment_colour, rect)

    def calculate_size(self, slider_container):
        '''Works out size and positioning using slider container'''
        # Calculate width
        self.width = slider_container.width * self.relative_width
        # Calculate height
        self.height = slider_container.height * self.relative_height

        # position is half the difference with container plus the position of the container
        self.xpos = ((slider_container.width - self.width) / 2) + slider_container.xpos
        self.ypos = ((slider_container.height - self.height) / 2) + slider_container.ypos

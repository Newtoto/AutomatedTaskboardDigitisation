'''All classes which pertain to the slider control at the bottom of the page'''
import pygame

class SliderContainer:
    '''Contains all parts of the slider'''
    def __init__(self, screen, height_percentage, images):
        self.height_percentage = height_percentage
        self.resize(screen)
        self.slider = Slider(images)

    def draw(self, screen):
        '''Draws all parts of resized slider'''
        self.resize(screen)
        pygame.draw.rect(screen, (0, 0, 0), ((0, self.ypos), (self.width, self.height)))
        self.slider.draw_segments()

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
        print(self.segment_quantity)

    def draw_segments(self):
        '''Draws sement for each image in array'''

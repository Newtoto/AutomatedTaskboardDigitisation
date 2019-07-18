import pygame
from pygame.locals import *
from PIL import Image
import glob

from image_manager import Photo
from slider import SliderContainer

# Initialise pygame and window settings
pygame.init()
(width, height) = (1024, 800)
screen = pygame.display.set_mode((width, height), HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption('Taskboard Timeline')
WHITE = (255, 255, 255)

# Initalise text
pygame.font.init()
DATE_FONT = pygame.font.SysFont('Helvetica', 30)

# Initialise photos
IMAGES = []

# Add images in folder to array
for filename in glob.glob("../TaskboardTracker/Images/*.jpg"):
# For testing outside of a build use this line instead
#for filename in glob.glob("./Images/*.jpg"):
    image = Photo(filename)
    # Add first image to array
    if len(IMAGES) == 0:
        IMAGES.append(image)
    else:
        image_added = False
        # Add image in ordered location
        for x in range(0, len(IMAGES)):
            # If image order value is lower, it comes earlier
            if image.ordering_value < IMAGES[x].ordering_value:
                # Insert image before comparison and set flag
                IMAGES.insert(x, image)
                image_added = True
                # Image added, so break out
                break
        # Add image to end if not added
        if image_added == False:
            IMAGES.append(image)

print(IMAGES)

# Initialise slider
slider_height_percent = 0.1
SLIDER_CONTAINER = SliderContainer(screen, slider_height_percent, IMAGES)

def draw_all():
    '''Scales and draws all elements on the screen'''
    # Background colour
    screen.fill((WHITE))
    # Draw scaled image and date text
    IMAGES[SLIDER_CONTAINER.slider.current_image].draw(screen, DATE_FONT, width, height * (1 - slider_height_percent))
    # Scale slider
    SLIDER_CONTAINER.resize(screen)
    # Draw slider
    SLIDER_CONTAINER.draw(screen)
    SLIDER_CONTAINER.slider.draw_draggable_object(screen)
    # Update all changed screen elements
    pygame.display.update()

def draw_slider():
    '''Only draw slider elements'''
    SLIDER_CONTAINER.draw(screen)

def move_slider():
    '''Checks mouse click and allows dragging of the slider'''
    if pygame.mouse.get_pressed()[0] == 1:
        SLIDER_CONTAINER.slider.drag(pygame.mouse.get_pos())
        if SLIDER_CONTAINER.slider.current_image != SLIDER_CONTAINER.slider.calculate_image():
            SLIDER_CONTAINER.slider.current_image = SLIDER_CONTAINER.slider.calculate_image()
            draw_all()
        else:
            SLIDER_CONTAINER.draw(screen)

# Show initial image
draw_all()

# Main loop
RUNNING = True

while RUNNING:

    move_slider()

    for event in pygame.event.get():
        # Exit on close button press
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        # Window has been resized
        if event.type == pygame.VIDEORESIZE:
            (width, height) = (event.w, event.h)
            screen = pygame.display.set_mode((width, height), HWSURFACE|DOUBLEBUF|RESIZABLE)
            # Scale and redraw screen
            draw_all()
            
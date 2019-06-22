import pygame
from pygame.locals import *

from image_manager import Photo
from slider import SliderContainer

# Initialise pygame and window settings
pygame.init()
(width, height) = (1920, 1080)
screen = pygame.display.set_mode((width, height), HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption('Taskboard Timeline')
WHITE = (255, 255, 255)

# Initalise text
pygame.font.init()
DATE_FONT = pygame.font.SysFont('Helvetica', 30)

# Initialise photos
photo0 = Photo("./Images/2019-02-28/taskboardImage_12-58-25.jpg")
photo1 = Photo("./Images/2019-02-28/taskboardImage_13-00-10.jpg")
photo2 = Photo("./Images/2019-02-28/taskboardImage_13-04-56.jpg")

IMAGES = [photo0, photo1, photo2]

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
        # # Mouse button has been clicked
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     # Increments current image if left mouse is clicked, does not if it isn't
        #     SLIDER_CONTAINER.slider.current_image += pygame.mouse.get_pressed()[0]
            
        #     # Wrap to first image when end is reached
        #     if SLIDER_CONTAINER.slider.current_image == len(IMAGES):
        #         SLIDER_CONTAINER.slider.current_image = 0
                
        #     # Redraw screen
        #     draw()
            
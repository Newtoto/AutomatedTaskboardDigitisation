import pygame
from pygame.locals import *

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
PRE_SPRINT_IMAGE = Photo("./Images/taskboardImage_2019-06-03_9-00.jpg")
DAY_1_PHOTO = Photo("./Images/taskboardImage_2019-06-03_10-00.jpg")
DAY_2_PHOTO = Photo("./Images/taskboardImage_2019-06-04_10-00.jpg")
DAY_3_PHOTO = Photo("./Images/taskboardImage_2019-06-05_10-00.jpg")
DAY_4_PHOTO = Photo("./Images/taskboardImage_2019-06-06_10-00.jpg")
DAY_5_PHOTO = Photo("./Images/taskboardImage_2019-06-07_10-00.jpg")
DAY_6_PHOTO = Photo("./Images/taskboardImage_2019-06-10_10-00.jpg")
DAY_7_PHOTO = Photo("./Images/taskboardImage_2019-06-11_10-00.jpg")
DAY_8_PHOTO = Photo("./Images/taskboardImage_2019-06-12_10-00.jpg")
DAY_9_PHOTO = Photo("./Images/taskboardImage_2019-06-13_10-00.jpg")
DAY_10_PHOTO = Photo("./Images/taskboardImage_2019-06-14_10-00.jpg")
END_SPRINT_IMAGE = Photo("./Images/taskboardImage_2019-06-14_17-00.jpg")

IMAGES = [PRE_SPRINT_IMAGE, DAY_1_PHOTO, DAY_2_PHOTO, DAY_3_PHOTO, DAY_4_PHOTO, DAY_5_PHOTO, DAY_6_PHOTO, DAY_7_PHOTO, DAY_8_PHOTO, DAY_9_PHOTO, DAY_10_PHOTO,END_SPRINT_IMAGE,]

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
            
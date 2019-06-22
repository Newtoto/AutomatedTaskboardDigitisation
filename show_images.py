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
myfont = pygame.font.SysFont('Helvetica', 30)

# Initialise photos
photo0 = Photo("./Images/2019-02-28/taskboardImage_12-58-25.jpg")
photo1 = Photo("./Images/2019-02-28/taskboardImage_13-00-10.jpg")
photo2 = Photo("./Images/2019-02-28/taskboardImage_13-04-56.jpg")

IMAGES = [photo0, photo1, photo2]

currentImage = 0

# Initialise slider
slider_height_percent = 0.1
SLIDER = SliderContainer(screen, slider_height_percent, IMAGES)

def draw():
    # Background colour
    screen.fill((WHITE))
    # Scale image
    IMAGES[currentImage].resize(width, height * (1 - slider_height_percent))
    # Draw image and date text
    IMAGES[currentImage].draw(screen, myfont)
    # Draw slider
    SLIDER.draw(screen)

    # Update all changed screen elements
    pygame.display.update()

# Show initial image
draw()

# Main loop
RUNNING = True

while RUNNING:

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
            draw()
        # Mouse button has been clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Increments current image if left mouse is clicked, does not if it isn't
            currentImage += pygame.mouse.get_pressed()[0]
            
            # Wrap to first image when end is reached
            if currentImage == len(IMAGES):
                currentImage = 0
                
            # Redraw screen
            draw()
            
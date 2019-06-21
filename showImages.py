import pygame
from pygame.locals import *

from imageManager import Photo

# Initialise pygame and window settings
pygame.init()
(width, height) = (600, 400)
screen = pygame.display.set_mode((width, height), HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption('Taskboard Timeline')

# Initalise text
pygame.font.init()
myfont = pygame.font.SysFont('Helvetica', 30)

# Initialise photos
photo0 = Photo("./Images/2019-02-28/taskboardImage_12-58-25.jpg")
photo1 = Photo("./Images/2019-02-28/taskboardImage_13-00-10.jpg")
photo2 = Photo("./Images/2019-02-28/taskboardImage_13-04-56.jpg")

IMAGES = [photo0, photo1, photo2]

currentImage = 0

def updateImage():
    # Only update when image is changed
    IMAGES[currentImage].resize(width, height)
    IMAGES[currentImage].draw(screen)
    # Write text
    dateText = myfont.render(IMAGES[currentImage].dateText, False, (0, 0, 0))
    timeText = myfont.render(IMAGES[currentImage].timeText, False, (0, 0, 0))
    screen.blit(dateText,(0, 0))
    screen.blit(timeText,(0, 30))
    
    # Update all changed screen elements
    pygame.display.update()

# Show initial image
updateImage()

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
            updateImage()
        # Mouse button has been clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if currentImage == len(IMAGES) - 1:
                currentImage = 0
            else:
                # Increments current image if left mouse is clicked, does not if it isn't
                currentImage += pygame.mouse.get_pressed()[0]
            # Display new image
            updateImage()
            
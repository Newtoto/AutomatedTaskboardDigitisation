import pygame
from pygame.locals import *

from imageManager import Photo

print("Oi oi")

pygame.init()
(width, height) = (600, 400)
screen = pygame.display.set_mode((width, height), HWSURFACE|DOUBLEBUF|RESIZABLE)
pygame.display.set_caption('Taskboard Timeline')

# Initialise photos
photo0 = Photo("./Images/2019-02-28/taskboardImage_12-58-25.jpg")
photo1 = Photo("./Images/2019-02-28/taskboardImage_13-00-10.jpg")
photo2 = Photo("./Images/2019-02-28/taskboardImage_13-04-56.jpg")

images = [photo0, photo1, photo2]

currentImage = 0

RUNNING = True

while RUNNING:
    
    images[currentImage].resize(width, height)
    images[currentImage].draw(screen)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.VIDEORESIZE:
            (width, height) = (event.w, event.h)
            screen = pygame.display.set_mode((width, height), HWSURFACE|DOUBLEBUF|RESIZABLE)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(currentImage == len(images) - 1):
                currentImage = 0
            else:
                # Increments current image if left mouse is clicked, does not if it isn't
                currentImage += pygame.mouse.get_pressed()[0]

        # Update all changed screen elements
        pygame.display.update()
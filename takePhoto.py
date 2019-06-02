from picamera import PiCamera
import time
import datetime
import pygame
import os

pygame.init()
(width, height) = (600, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.flip

#Take photo and make directory
def TakePhoto():
    camera.start_preview(alpha=200)
    # Allow camera to focus
    time.sleep(10)
    # Set image directory target for each day
    dailyDirectoryName = './' + time.strftime("%Y-%m-%d/")
    if not os.path.exists(dailyDirectoryName):
        os.makedirs(dailyDirectoryName)
    # Save image and append time
    camera.capture(dailyDirectoryName + 'taskboardImage' + time.strftime("_%H-%M-%S") + '.jpg')
    # Put camera back to sleep
    camera.stop_preview()
    
# Used if specific times are desired rather than hourly photos
# Time is 9:00
photoTime1 = '09'
# Time is 17:00
photoTime2 = '17'
        
running = True

camera = PiCamera()

# TakePhoto()

while running:
    
    # Check if minutes is 00, to trigger only 1 photo per hour
    if time.strftime("%M%S") == "0000":
        TakePhoto()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                running = False
            elif event.key == pygame.K_p:
                TakePhoto()
'''Controlls constant photographing from a raspberry pi camera'''
import time
import os

import pygame

from picamera import PiCamera

# Pygame is used as a means of exiting and testing the camera
pygame.init()
(WIDTH, HEIGHT) = (600, 400)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#Take photo and make directory
def take_photo():
    '''Takes photo and saves to specified directory with timestamp'''
    CAMERA.start_preview(alpha=200)
    # Allow camera to focus
    time.sleep(10)
    # Set image directory target for each day
    daily_directory_name = './Images/' + time.strftime("%Y-%m-%d/")
    if not os.path.exists(daily_directory_name):
        os.makedirs(daily_directory_name)
    # Save image and append time
    CAMERA.capture(daily_directory_name + 'taskboardImage' + time.strftime("_%H-%M-%S") + '.jpg')
    # Put camera back to sleep
    CAMERA.stop_preview()

# Used if specific times are desired rather than hourly photos
# Time is 9:00
PHOTO_TIME_1 = '09'
# Time is 17:00
PHOTO_TIME_2 = '17'

RUNNING = True

CAMERA = PiCamera()

# TakePhoto()

while RUNNING:

    # Check if minutes is 00, to trigger only 1 photo per hour
    if time.strftime("%M%S") == "0000":
        take_photo()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                running = False
            elif event.key == pygame.K_p:
                take_photo()
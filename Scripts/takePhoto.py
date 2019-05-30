from picamera import PiCamera
import time
import datetime

# Used if specific times are desired rather than hourly photos
# Time is 9:00
photoTime1 = '09'
# Time is 17:00
photoTime2 = '17'

running = true

camera = PiCamera()

while running:
    # Check if minutes is 00, to trigger only 1 photo per hour
    if time.strftime("%M") == "00":
        # Allow camera to focus
        camera.start_preview()
        sleep(10)
        # Set image directory target for each day
        dailyDirectoryName = 'home/pi/' + time.strftime("-%Y-%m-%d/")
        # Save image and append time
        camera.capture(dailyDirectoryName + 'taskboardImage' + time.strftime("_%H%M") + '.jpg')
        # Put camera back to sleep
        camera.stop_preview()


import cv2
import numpy as np

# Read image from file with openCV
image = cv2.imread('../Images/TaskboardTestImage.jpg')

# Turn image greyscale
taskboardImage = np.copy(image)
gray = cv2.cvtColor(taskboardImage, cv2.COLOR_RGB2GRAY)
# Apply gaussian blur to image
blur = cv2.GaussianBlur(gray, (5,5), 0)

canny = cv2.Canny(blur, 50, 150)

cv2.imshow('result', canny)
# Display image for set time in ms
cv2.waitKey(0)
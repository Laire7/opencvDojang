import sys
import numpy as np
import cv2

# Callback function for the trackbar
def on_trackbar(pos):
    # Get the current positions of the trackbars
    hmin = cv2.getTrackbarPos('H_min', 'Trackbar')
    hmax = cv2.getTrackbarPos('H_max', 'Trackbar')
    smin = cv2.getTrackbarPos('S_min', 'Trackbar')
    smax = cv2.getTrackbarPos('S_max', 'Trackbar')


    # Apply the inRange function to create a mask based on the current trackbar values
    dst = cv2.inRange(src_hsv, (hmin, smin, 0), (hmax, smax, 255))

    # Display the masked image
    cv2.imshow('Trackbar', dst)

# Load the image
fileName = 'snack/blueberry/10060_0_s_2.jpg'
src = cv2.imread(fileName)
src = cv2.resize(src, (1000,1000))

# Check if the image was loaded correctly
if src is None:
    sys.exit("Image Load failed!")

# Convert the image from BGR to HSV color space
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# Create a window
cv2.namedWindow('Trackbar')

# Create the trackbars for adjusting the hue (H_min and H_max)
cv2.createTrackbar('H_min', 'Trackbar', 0, 255, on_trackbar)
cv2.createTrackbar('H_max', 'Trackbar', 0, 255, on_trackbar)
cv2.createTrackbar('S_min', 'Trackbar', 0, 255, on_trackbar)
cv2.createTrackbar('S_max', 'Trackbar', 0, 255, on_trackbar)

# Initialize the trackbar position and show the initial result
on_trackbar(0)

# Keep updating the window until 'q' is pressed
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

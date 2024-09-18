import cv2
import numpy as np

def detect_traffic_light(image):
    """Detects the color of a traffic light in an image.

    Args:
        image: The input image.

    Returns:
        The color of the traffic light ('red', 'yellow', or 'green'), or None if no traffic light is detected.
    """

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color ranges for red, yellow, and green
    red_lower = np.array([0, 100, 100])
    red_upper = np.array([10, 255, 255])
    yellow_lower = np.array([15, 100, 100])
    yellow_upper = np.array([35, 255, 255])
    green_lower = np.array([45, 100, 100])
    green_upper = np.array([75, 255, 255])

    # Create masks for each color range
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    green_mask = cv2.inRange(hsv, green_lower, green_upper)   


    # Find contours in each mask
    red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    yellow_contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)   
    green_contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)   


    # Find the largest contour for each color
    largest_red_contour = None
    largest_yellow_contour = None
    largest_green_contour = None
    if red_contours:
        largest_red_contour = max(red_contours, key=lambda c: cv2.contourArea(c))
    if yellow_contours:
        largest_yellow_contour = max(yellow_contours, key=lambda c: cv2.contourArea(c))
    if green_contours:
        largest_green_contour = max(green_contours, key=lambda c: cv2.contourArea(c))

    # Determine the color of the traffic light based on the largest contour
    if largest_red_contour:
        return 'red'
    elif largest_yellow_contour:
        return 'yellow'
    elif largest_green_contour:
        return 'green'
    else:
        return None

# Load the image
image = cv2.imread('traffic_light.jpg')

# Detect the color of the traffic light
color = detect_traffic_light(image)

# Print the result
if color:
    print(f"The traffic light is {color}.")
else:
    print("No traffic light detected.")
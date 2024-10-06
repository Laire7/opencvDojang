import cv2
import numpy as np

def nothing(x):
    pass

# Load the image
img = cv2.imread('snack/blueberry/10060_0_s_2.jpg')

# Check if image loaded
if img is None:
    print("Error: Could not load image.")
    exit()

# Convert the image to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range of yellow color in HSV
# lower_yellow = np.array([20, 100, 100])
# upper_yellow = np.array([30, 255, 255])

# Define the color range for the blue Pocky (adjust as needed)
lower_blue = np.array([110, 0, 0])
upper_blue = np.array([195, 255, 255])

# Create a mask for yellow color
color_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

# Create a window and trackbars for adjusting the hue of the yellow areas
cv2.namedWindow('Color Adjuster')

cv2.createTrackbar('Hue', 'Color Adjuster', 0, 255, nothing)  # Set hue initially to purple (120-150)

while True:
    # Get trackbar positions for hue, saturation, and value
    h = cv2.getTrackbarPos('Hue', 'Color Adjuster')

    # Create an HSV version of the yellow mask with the new hue, saturation, and value
    modified_hsv = hsv_img.copy()
    modified_hsv[color_mask > 0] = [h,]

    # Convert back to BGR to display
    modified_img = cv2.cvtColor(modified_hsv, cv2.COLOR_HSV2BGR)

    # Combine the original image with the modified parts
    final_img = cv2.bitwise_and(modified_img, modified_img, mask=color_mask)  # Apply color change to yellow parts
    final_img = cv2.add(final_img, cv2.bitwise_and(img, img, mask=cv2.bitwise_not(color_mask)))  # Keep other parts intact

    # Show the final image with color adjustments
    cv2.imshow('Color Adjuster', final_img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

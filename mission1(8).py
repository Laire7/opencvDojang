import cv2
import numpy as np

# Load the image
image = cv2.imread("misson/01.png")
src = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED)

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a mask for pixels with h value at least 100
mask = hsv[:, :, 0] >= 50

# Convert the mask to 8-bit unsigned integer
mask = mask.astype(np.uint8)

# Apply the mask to the original image
result = image.copy()
result[~mask] = 0 # Set pixels outside the mask to black

# Apply denoise
denoise = cv2.fastNlMeansDenoisingColored(src,None,10,10,21,21)

# Copy denoised pixels to result where mask is 1
cv2.copyTo(denoise, result, mask)

# Display the result
cv2.imshow("Result", result)
cv2.imshow("Denoised Image with mask", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
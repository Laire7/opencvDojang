import cv2
import numpy as np

# Load the image
image = cv2.imread("misson/01.png")
src = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED)
org = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED)

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a mask for pixels with h value at least 100
mask = hsv[:, :, 0] >= 50

# Apply the mask to the original image
result = image.copy()
result[~mask] = 0  # Set pixels outside the mask to black
result = mask.astype(np.uint8)

# Apply denoise
denoise = cv2.fastNlMeansDenoisingColored(src,None,10,10,21,21)

# Apply denoise with mask
cv2.copyTo(denoise, result, src)

# Create a sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
src = cv2.filter2D(src, -1, kernel)

# Display the result
cv2.imshow("Original", org)
cv2.imshow("Denoised Image with mask, then sharpen", src)
cv2.waitKey()
cv2.destroyAllWindows()
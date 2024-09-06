import cv2

# Load the image
image = cv2.imread('misson/05.png')

# Scale down brightness for overexposed areas
alpha = 0.8  # Simple contrast control
beta = -50   # Simple brightness control

adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Show the adjusted image
cv2.imshow('Original Image', image)
cv2.imshow('Adjusted Image', adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

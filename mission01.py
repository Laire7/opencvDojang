import cv2

def denoise_sky(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the range for the sky (adjust as needed)
    lower_sky = np.array([0, 0, 100])  # Adjust the lower bound for hue, saturation, and value
    upper_sky = np.array([180, 255, 255])  # Adjust the upper bound

    # Create a mask for the sky
    mask = cv2.inRange(hsv, lower_sky, upper_sky)

    # Apply Gaussian blur to the masked image to denoise the sky
    blurred_mask = cv2.GaussianBlur(mask, (5, 5), 0)  # Adjust kernel size and sigmaX

    # Create a new image with the denoised sky
    denoised_img = img.copy()
    denoised_img[blurred_mask == 0] = 0

    return denoised_img

# Example usage
image_path = "your_image.jpg"
denoised_img = denoise_sky(image_path)

# Display the denoised image
cv2.imshow("Denoised Image", denoised_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
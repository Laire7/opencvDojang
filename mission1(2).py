import cv2
import numpy as np

def denoise_low_brightness(image, threshold=40, filter_type='gaussian', kernel_size=(5, 5)):
    """Applies denoise filter to pixels with brightness less than a threshold.

    Args:
        image: The input image.
        threshold: The brightness threshold (default: 40).
        filter_type: The type of denoise filter ('gaussian', 'bilateral').
        kernel_size: The kernel size for the denoise filter.

    Returns:
        The denoised image.
    """

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a mask for low-brightness pixels
    mask = gray < threshold

    # Apply denoise filter to masked pixels
    if filter_type == 'gaussian':
        denoised_mask = cv2.GaussianBlur(gray[mask], kernel_size, 0)
    elif filter_type == 'bilateral':
        denoised_mask = cv2.bilateralFilter(gray[mask], -1, 10, 10)  # Adjust parameters as needed
    else:
        raise ValueError("Invalid filter type. Choose 'gaussian' or 'bilateral'.")

    # Combine denoised pixels with original pixels
    denoised_image = image.copy()
    denoised_image[mask] = cv2.cvtColor(denoised_mask, cv2.COLOR_GRAY2BGR)

    return denoised_image

# Example usage
image_path = "misson/01.jpg"
image = cv2.imread(image_path)

denoised_image = denoise_low_brightness(image, threshold=40, filter_type='gaussian')

cv2.imshow("Original Image", image)
cv2.imshow("Denoised Image", denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
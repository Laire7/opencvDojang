import cv2
import numpy as np

orig_img = cv2.imread('misson/01.png', cv2.IMREAD_UNCHANGED)
# Convert the image to HSV color space
orig_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)[...,::-1]

# Create a sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

dst = cv2.filter2D(orig_img, -1, kernel)
dst = cv2.fastNlMeansDenoisingColored(orig_img,None,10,10,7,21)

# Apply the sharpening filter

# plt.subplot(121), plt.imshow(orig_img),plt.title("Original Image")
# plt.subplot(122), plt.imshow(dst), plt.title("Denoised Image")
cv2.imshow('src1', orig_img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
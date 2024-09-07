import cv2
img = cv2.imread('../data2/lenna.bmp')

if img is None:
    print("Image not found")

img[100:400, 200:300, 0] = 255
img[100:400, 200:300, 1] = 255
img[100:400, 200:300, 2] = 255

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
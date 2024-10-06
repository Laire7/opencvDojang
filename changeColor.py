# import required libraries
import cv2
import numpy as np

def nothing(x):
   pass
   
# Create a black image, and the window
img = np.zeros((300,650,3), np.uint8)
window_name = 'Trackbar Color Palette'
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

# create trackbars for color change
cv2.createTrackbar('R',window_name,0,255,nothing)
cv2.createTrackbar('G',window_name,0,255,nothing)
cv2.createTrackbar('B',window_name,0,255,nothing)
while(True):
   cv2.imshow(window_name,img)
   k = cv2.waitKey(1) & 0xFF
   if k == ord('q'):
      break
      
   # get current positions of four trackbars
   r = cv2.getTrackbarPos('R',window_name)
   g = cv2.getTrackbarPos('G',window_name)
   b = cv2.getTrackbarPos('B',window_name)
   img[:] = [b,g,r]
cv2.destroyAllWindows()
import cv2

# main
while True:
    key = cv2.waitKeyEx(30)
    if key == 0x00250000:
        print("Shift key pressed")
    
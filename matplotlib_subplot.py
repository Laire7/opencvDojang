# 이미지를 4장 불러온다
# 이미지를 4장을 하나의 창에 띄운다

import cv2, sys
from matplotlib import pyplot as plt

# 이미지 4장 가져오기
imgBGR1 = cv2.imread('data/lena.jpg')
imgBGR3 = cv2.imread('data/orange.jpg')
imgBGR4 = cv2.imread('data/apple.jpg')
imgBGR2 = cv2.imread('data/baboon.jpg')

if imgBGR1 is None or imgBGR2 is None \
    or imgBGR3 is None or imgBGR4 is None:
    sys.exit("image load is failed")

imgRBG1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgRBG2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgRBG3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGR2RGB)
imgRBG4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGR2RGB)

# matplotlib plt.subplot로 이미지를 출력
figsize = (10,10)
fig, ax = plt.subplots(2,2, figsize=figsize)
ax[0][0].axis('off')
ax[0][1].axis('off')
ax[1][0].axis('off')
ax[1][1].axis('off')

ax[0][0].imshow(imgRBG1, aspect='auto')
ax[0][1].imshow(imgRBG3, aspect='auto')
ax[1][0].imshow(imgRBG4, aspect='auto')
ax[1][1].imshow(imgRBG2, aspect='auto')

ax[0][0].title('Lena')
ax[0][1].title('Orange')
ax[1][0].title('Apple')
ax[1][1].title('Baboon')
fig.suptitle('Sample windows')
fig.canvas.manager.set_window_title('Sample windows')
plt.show()
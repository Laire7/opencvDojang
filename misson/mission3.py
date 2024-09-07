import cv2
image = cv2.imread('misson/05.png')

#ConvertScaleAbs 이미지 필터 적용
# 대비효과를 극대화 보다 낯추려고 하는 것 처럼 보이는데 
# beta 값으로 밝기를 낮추어 검정에 가까운 픽셀들을 다 0(검정)으로 되게 만들고, 노출 과다를 처리한다 
alpha = 0.8  # 대비 (곱셈) alpha<1 극소화, alpha>1 극대화
beta = -50   # 밝기 (덧셈) beta<0 어둡게, beta>0 밝게
adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# 이미지 출력
cv2.imshow('Original Image', image)
cv2.imshow('Adjusted Image', adjusted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

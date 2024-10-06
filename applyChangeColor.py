import numpy as np
from transformData import Transform, DataAug

banana_imgPath = 'snack/banana/10095_0_s_2.jpg'
banana_mask_range_lower = np.array([20, 100, 100])
banana_mask_range_upper = np.array([30, 255, 255])
banana_hmin = 120
banana_hmax = 160

bananaAug = Transform(banana_imgPath)
bananaAug.changeColor(banana_mask_range_lower, banana_mask_range_upper, banana_hmin, banana_hmax)

blueberry_imgPath = 'snack/blueberry/10060_0_s_2.jpg'
blueberry_mask_range_lower = np.array([110, 0, 0])
blueberry_mask_range_upper = np.array([195, 255, 255])
blueberry_hmin = 200
blueberry_hmax = 210

bananaAug = Transform(blueberry_imgPath)
bananaAug.changeColor(blueberry_mask_range_lower, blueberry_mask_range_upper, blueberry_hmin, blueberry_hmax)
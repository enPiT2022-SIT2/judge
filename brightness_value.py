#coding: utf-8

import cv2
import numpy as np

#グレースケール化
img = cv2.imread('sample2.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
brightness_value_mean = np.average(img_gray)
#print(brightness_value_mean)

#cv2.imwrite('sample2_gray.jpg',img_gray)

#閾値と判定
threshold = 10
judge = 0

if brightness_value_mean  >= threshold:
    print("手詰まりしています！")

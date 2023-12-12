import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread('lena.jpg')

# 中心軸に関して左右反転
flipped_image = cv2.flip(image, 1)

# 画像の表示
cv2.imshow('Image', image)
cv2.imshow('Flipped Image', flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

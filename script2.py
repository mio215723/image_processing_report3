import cv2
import numpy as np

def alpha_blend(image1, image2, alpha):
    # アルファブレンディングの実行
    blended = cv2.addWeighted(image1, alpha, image2, 1 - alpha, 0)
    return blended

# 二つの入力画像の読み込み
image1 = cv2.imread('clothe.jpg')
image2 = cv2.imread('lena.jpg')

# アルファブレンディングの割合（例: 0.7）
alpha_value = 0.7

# アルファブレンディングの実行
blended_image = alpha_blend(image1, image2, alpha_value)

# 元の画像とブレンディング後の画像を表示
cv2.imshow('Image1', image1)
cv2.imshow('Image2', image2)
cv2.imshow('Blended Image', blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

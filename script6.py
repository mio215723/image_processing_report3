import cv2
import numpy as np


def make_sharp_kernel(k: int):
  return np.array([
    [-k / 9, -k / 9, -k / 9],
    [-k / 9, 1 + 8 * k / 9, k / 9],
    [-k / 9, -k / 9, -k / 9]
  ], np.float32)

input_image = cv2.imread("./lena.jpg")
kernel_4 = make_sharp_kernel(4)
kernel_9 = make_sharp_kernel(9)
kernel_18 = make_sharp_kernel(18)
sharpened_image_4x = cv2.filter2D(input_image, -1, kernel_4).astype("uint8")
sharpened_image_9x = cv2.filter2D(input_image, -1, kernel_9).astype("uint8")
sharpened_image_18x = cv2.filter2D(input_image, -1, kernel_18).astype("uint8")

cv2.imshow('Original Image', input_image)
cv2.imshow('Sharpened Image (4x)', sharpened_image_4x)
cv2.imshow('Sharpened Image (9x)', sharpened_image_9x)
cv2.imshow('Sharpened Image (18x)', sharpened_image_18x)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

def apply_average_filter(image, kernel_size):
    # カーネルの生成
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)

    # フィルタの適用
    filtered_image = cv2.filter2D(image, -1, kernel)

    return filtered_image

def apply_weighted_average_filter(image, kernel_size):
    # カーネルの生成
    weights = create_weight_matrix(kernel_size)
    kernel = weights / np.sum(weights)

    # フィルタの適用
    filtered_image = cv2.filter2D(image, -1, kernel)

    return filtered_image

def create_weight_matrix(kernel_size):
    # 重み行列の生成
    weights = np.zeros((kernel_size, kernel_size), dtype=np.float32)
    center = (kernel_size - 1) // 2

    for i in range(kernel_size):
        for j in range(kernel_size):
            distance = np.sqrt((i - center)**2 + (j - center)**2)
            weights[i, j] = 1 / (1 + distance)

    return weights

# 画像の読み込み
input_image = cv2.imread('lena.jpg')

# 3x3平均化フィルタの適用
filtered_image_3x3 = apply_average_filter(input_image, 3)
filtered_weighted_image_3x3 = apply_weighted_average_filter(input_image, 3)


# 5x5平均化フィルタの適用
filtered_image_5x5 = apply_average_filter(input_image, 5)
filtered_weighted_image_5x5 = apply_weighted_average_filter(input_image, 5)

# 元画像とフィルタ適用後の画像を表示
cv2.imshow('Original Image', input_image)
cv2.imshow('3x3 Average Filtered Image', filtered_image_3x3)
cv2.imshow('3x3 Average Filtered Weighted Image', filtered_weighted_image_3x3)
cv2.imshow('5x5 Average Filtered Weighted Image', filtered_image_5x5)
cv2.imshow('5x5 Average Filtered Image', filtered_weighted_image_5x5)
cv2.waitKey(0)
cv2.destroyAllWindows()

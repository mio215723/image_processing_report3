import cv2
import numpy as np

def extract_contours(image_path):
    # 画像をグレースケールで読み込む
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 画像のぼかしを行い、ノイズを軽減する
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Cannyエッジ検出を行う
    edges = cv2.Canny(blurred, 50, 150)

    # 輪郭抽出
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 元の画像に輪郭を描画する
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)

    # 結果を表示
    cv2.imshow('Original Image', image)
    cv2.imshow('Image with Contours', image_with_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 画像のパスを指定して輪郭を抽出
extract_contours('./lena.jpg')

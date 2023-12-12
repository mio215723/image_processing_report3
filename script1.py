import cv2
import numpy as np

def gamma_correction(image, gamma):
    # 画像の各ピクセルに対してγ変換を適用
    gamma_corrected = np.power(image/255.0, gamma) * 255.0
    # ピクセル値を0から255の範囲にクリップ
    gamma_corrected = np.clip(gamma_corrected, 0, 255).astype(np.uint8)
    return gamma_corrected

# 入力画像の読み込み
input_image = cv2.imread("./lena.jpg")

# γ変換のパラメータ（例: 2.0）
gamma_value = 2.0

# γ変換の実行
output_image = gamma_correction(input_image, gamma_value)

# 変換前後の画像を表示
cv2.imshow('Input Image', input_image)
cv2.imshow('Gamma Corrected Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

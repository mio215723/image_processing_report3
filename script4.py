import cv2
import numpy as np
import time
import random

def split_image(image, rows, cols):
    height, width, _ = image.shape
    tile_height = height // rows
    tile_width = width // cols
    tiles = []
    for i in range(rows):
        for j in range(cols):
            tile = image[i * tile_height: (i + 1) * tile_height, j * tile_width: (j + 1) * tile_width]
            tiles.append(tile)
    return tiles

def display_and_flip_tiles(tiles):
    for tile in tiles:
        # 中心軸に関して左右反転
        flipped_tile = cv2.flip(tile, 1)

        # タイルを表示
        cv2.imshow('Flipping Tiles', flipped_tile)
        print(flipped_tile.shape)
        cv2.waitKey(5000)  # 5秒待機
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # 画像の読み込み
    original_image = cv2.imread('lena.jpg')

    # 画像を3x3のモザイクタイル状に分割
    mosaic_tiles = split_image(original_image, 3, 3)

    # タイルをランダムにシャッフル
    random.shuffle(mosaic_tiles)

    # 各タイルを順番にまたはランダムに選んで5秒ごとに左右反転して表示
    display_and_flip_tiles(mosaic_tiles)

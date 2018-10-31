# mosaic関数作成
import cv2

def mosaic(img, rect, size):
    # モザイクかける領域取得
    # 左上、右下のx,y代入
    (x1,y1 ,x2 ,y2 ) = rect
    # 横幅取得
    w = x2 - x1
    # 縦幅取得
    h = y2 - y1
    # 取得した位置の部分をi_rectに代入
    i_rect = img[y1:y2,x1:x2]
    # 一度縮小して拡大する
    # I_rectのモザイク対象部分の画像をsizeの大きさの正方形にする→i_small
    i_small = cv2.resize(i_rect, (size,size))
    #  小さくした画像をモザイク対象範囲の大きさに拡大→i_mos
    # 拡大縮小の方法　interpolation = cv2.INTER_AREA（平均画素法）
    i_mos = cv2.resize(i_small, (w ,h), interpolation = cv2.INTER_AREA)

    # 画像にモザイク画像を重ねる
    img2 = img.copy()
    # モザイク対象範囲にモザイク化した画像を代入
    img2[y1:y2, x1:x2] = i_mos
    return img2

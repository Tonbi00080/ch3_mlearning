import cv2
import numpy as np

# Webカメラから入力を開始
# 撮影のためのobject生成
cap = cv2.VideoCapture(0)
while True:
    # カメラの画像を読み込む　_:T/f読み込めたか、frame:画像
    _, frame = cap.read()
    # 画像を縮小表示する
    frame = cv2.resize(frame, (500,300))
    # hsv変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
    # 画像numpy配列[行,列,色(HSV)]
    h = hsv[:,:,0] # 色相
    s = hsv[:,:,1] # 彩度
    v = hsv[:,:,2] # 明度
    # 赤色っぽい色のみ抽出
    # uint8だから０整数　# hの型に合わせる
    # 要素０の配列生成 numpy.zeros(shape, dtype = float, order = ‘C’)
    img = np.zeros(h.shape, dtype = np.uint8)
    # 赤っぽい色に白(255)代入
    img[((h < 50) | (h > 200)) & (s > 100)] = 255
    # ウィンドウに画像を出力する
    # imshow('画像ファイル名',画像変数名)
    cv2.imshow('Red Camera', img)
    # ESCかEnterキーが押されたらループ抜ける
    # cv2.waitKey(t):tミリ秒キーボード入力を受け付ける
    k = cv2.waitKey(1) #1msec確認
    # 27:esc,13:enter
    if k == 27 or k == 13: break

cap.release() #カメラ解放
cv2.destoryAllWindows() #ウィンドウ破棄

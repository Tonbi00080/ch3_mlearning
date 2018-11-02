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
    # 画像numpy配列[行,列,色(BGR)]
    frame[:,:,0] = 0 # 青要素０
    frame[:,:,1] = 0 # 緑要素０
    # ウィンドウに画像を出力する
    # imshow('画像ファイル名',画像変数名)
    cv2.imshow('Red Camera', frame)
    # ESCかEnterキーが押されたらループ抜ける
    # cv2.waitKey(t):tミリ秒キーボード入力を受け付ける
    k = cv2.waitKey(1) #1msec確認
    # 27:esc,13:enter
    if k == 27 or k == 13: break

cap.release() #カメラ解放
cv2.destoryAllWindows() #ウィンドウ破棄

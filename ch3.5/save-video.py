import cv2
import numpy as np

# カメラからの入力を開始
cap = cv2.VideoCapture(0)
# 動画書き出し用のオブジェクトを生成
fmt = cv2.VideoWriter_fourcc('m','p','4','v')
fps = 20.0
size = (640, 360)
# VideoWriter(動画ファイル名,フォーマット(fourcc),fps(１秒間のフレーム数),動画画面サイズ)
writer = cv2.VideoWriter('test.m4v', fmt, fps, size)

while True:
    _, frame = cap.read()
    # 画像を縮小
    frame = cv2.resize(frame,size)
    # 画像を出力する
    writer.write(frame)
    # ウィンドウにも表示
    cv2.imshow('frame',frame)
    # Enterで抜ける
    if cv2.waitKey(1) == 13:break

writer.release()
cap.release()
cv2.destroyAllWindows() # ウィンドウ破棄

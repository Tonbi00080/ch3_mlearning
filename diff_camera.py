import cv2

cap = cv2.VideoCapture(0)
img_last = None # 前回の画像を記憶する
green = (0,255,0)

while True:
    # 画像を取得
    _, frame = cap.read()
    frame = cv2.resize(frame, (500,300))
    # 白黒画像に変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (9,9), 0)
    img_b = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]
    # 差分を確認
    if img_last is None:
        img_last = img_b
        continue
    frame_diff = cv2.absdiff(img_last, img_b) # 画像の配列の差分を返す
    cnts =  cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1] # 輪郭値のリスト返す
    # 差分があった点を画面に描く
    for pt in cnts:
        x, y, w, h = cv2.boundingRect(pt) # 輪郭値をx,y,w,hに変換
        if w < 30: continue # 小さな変更点は無視
        cv2.rectangle(frame,(x,y),(x + w, y + h), green, 2)
    # 今回のフレーム保存
    img_last = img_b
    # 画像に表示
    cv2.imshow("Diff Camera", frame)
    cv2.imshow("diff data", frame_diff)
    # Enterで停止ß
    if cv2.waitKey(1) == 13: break
cap.release()
cv2.destroyAllWindows()

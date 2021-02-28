import cv2
import numpy as np
#%matplotlib inline
img = cv2.imread("white_line.png")
cv2.imshow("before.jpg", img)
height, width, channels = img.shape
print(img.shape)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,90,450,apertureSize = 3)
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/360, threshold=60, minLineLength=10, maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    red_line_img = cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 3)

for i in range(int(height/2)):
    test = red_line_img[303][0][0]
    counter = list.count(red_line_img[height - i -1][:][:])
    if counter == 4:
        print ('red_line')

cv2.imshow("output3.jpg", red_line_img)

'''
boundary = []
# 画像の幅だけループを実行
for (let i = 0; i < pixelArray.length; i++) {
  if (pixelArray[i] != pixelArray[i+1]){
    boundary.push(i);
  }
}

# 道路の中心座標を求める
let centerX = 0;
if (boundary.length >= 4){
  centerX = ((boundary[2] - boundary[1])/2) + boundary[1];
} else{
  centerX = 0;
}
       
# 左寄りを走行
if ((video.width/2-centerX) < -10){
  # ステアリングを右へ 
  motorSteer.reverse();
# 右寄りを走行
} else if ((video.width/2-centerX) > 10){
  # ステアリングを左へ
  motorSteer.forward();
# 車線中央から+/-10ピクセル以内
} else {
  # ステアリングを中央へ
  motorSteer.stop();
}       
  '''     
cv2.waitKey(0)
cv2.destroyAllWindows()
       
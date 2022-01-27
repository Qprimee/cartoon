import cv2
import numpy as np 



photo = "C:\Users\Modiran\Desktop\POR\pythons\machin\Face\\10.jpg"
img = cv2.imread(photo)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey = cv2.medianBlur(grey, 5)
ed = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#cartoonize
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask = ed)



oil = cv2.xphoto.oilPainting(img, 1, 1, cv2.COLOR_BGR2Lab)

cv2.imshow("Oilpainting", oil)
cv2.imshow("Cartoon", cartoon)


cv2.waitKey(0)



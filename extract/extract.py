import os
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, 'got.jpg')

frame = cv2.imread(img_path) # RGB Red Green Blue -> BGR Blue Green Red
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cv2.imshow("frame", frame)
cv2.imshow("gray", gray)
cv2.waitKey(0) # press w to quit
cv2.destroyAllWindows()
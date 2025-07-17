import cv2
import numpy as np


# img = cv2.imread('/Users/sushil/Desktop/deep-learning/istockphoto-529664572-612x612.jpg')

img = np.zeros((512,512,3))




def draw(event , x,y,flags,params):
  # print(event)
  if event == 1:
    cv2.circle(img , center=(x,y), radius=50, color=(255,0,0), thickness=-1)
    print("Mouse up clicked")

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window", draw)

while True:
  cv2.imshow("window", img)
  if cv2.waitKey(1) & 0xFF == ord('x'):
    break

cv2.destroyAllWindows()




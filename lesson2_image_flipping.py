import cv2
import numpy as np

img = cv2.imread("images/image2.jpg")
cv2.imshow("image2",img)
cv2.waitKey(0)

flip_img = cv2.flip(img,0)

cv2.imshow("image flipping ",flip_img)
cv2.waitKey(0)

flip_img = cv2.flip(img,1)

cv2.imshow("image flipping ",flip_img)
cv2.waitKey(0)

flip_img = cv2.flip(img,-1)

cv2.imshow("image flipping ",flip_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("images/image2.jpg")
cv.imshow("Original Image", img)

# Convert BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("BGR to Grayscale", gray)

# Convert BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)   
cv.imshow("BGR to HSV", hsv)

# Convert HSV back to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR", hsv_bgr) 

#Convert BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("BGR to LAB", lab)

#Convert LAB back to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB to BGR", lab_bgr)
cv.waitKey(0)
cv.destroyAllWindows()

#Convert BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("BGR to RGB", rgb)
plt.imshow(rgb)
plt.show()


import cv2 as cv
import numpy as np

img = cv.imread("images/image1.jpg")
img = cv.resize(img, (400, 300))
cv.imshow("Image", img)

# Create a blank image with the same dimensions as the original image
blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank Image", blank)

# Create a circular mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Mask", mask)

# Apply the mask to the image
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Image", masked)


blank1 = np.zeros(img.shape[:2], dtype="uint8")

# Create a rectangular mask
rectangle_mask = cv.rectangle(blank1, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)
cv.imshow("Rectangle Mask", rectangle_mask)

# Apply the rectangular mask to the image
rectangle_masked = cv.bitwise_and(img, img, mask=rectangle_mask)
cv.imshow("Rectangle Masked Image", rectangle_masked)

cv.waitKey(0)
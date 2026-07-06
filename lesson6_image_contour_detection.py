import cv2 as cv
import numpy as np

img = cv.imread("images/image2.jpg")
cv.imshow("Orginal image", img)

# Create a blank image with the same dimensions as the original image
blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Apply Gaussian blur to the grayscale image
blur = cv.GaussianBlur(gray, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Apply Canny edge detection to the blurred image
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

# Find contours in the image
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded", thresh)

# Find contours in the thresholded image
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contours found!")

# Draw contours on the blank image
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)
import cv2 as cv
import numpy as np

img = cv.imread("images/image2.jpg")

cv.imshow("Original Image", img)

# Create a blank image with the same dimensions as the original image
blank = np.zeros(img.shape[:2], dtype="uint8")

# Split the image into its color channels
b, g, r = cv.split(img)

cv.imshow("Blue", b)
cv.imshow("Green", g)       
cv.imshow("Red", r)

# Merge the color channels back into a single image
merged = cv.merge([b, g, r])
cv.imshow("Merged Image", merged)

# Create images for each color channel
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue Channel", blue)
cv.imshow("Green Channel", green)
cv.imshow("Red Channel", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)
cv.destroyAllWindows()
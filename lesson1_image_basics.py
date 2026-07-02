import cv2
import numpy as np

# Load image and reade

img = cv2.imread("images/image1.jpg")


print(type(img))
print(img.shape) 

# image resize
re_img = cv2.resize(img,(500,400))

cv2.imshow('Resize imge',re_img)
cv2.waitKey(0)

# image convert to grayscale

img_gray = cv2.cvtColor(re_img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)

cv2.imshow('Convert Grayscale color',img_gray)
cv2.waitKey(0)

# Playing with RGB channels
# remove blue color
re_img[:,:,0] = 0
cv2.imshow('Remove Blue color',re_img)
cv2.waitKey(0)

#remove green color
re_img[:,:,1] = 0
cv2.imshow('Remove Green color',re_img)
cv2.waitKey(0)

#remove red color
re_img = cv2.resize(img,(500,400))
re_img[:,:,2] = 0
cv2.imshow('Remove Red color',re_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

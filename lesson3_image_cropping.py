import cv2

img = cv2.imread("images/image3.jpg")
cv2.imshow('image3',img)
cv2.waitKey(0)

crop_img = img[0:400, 0:500]

# crope image save
cv2.imwrite("Flower_crop.jpg", crop_img)
cv2.imshow('After cropping',crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
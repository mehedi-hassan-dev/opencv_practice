import cv2
import numpy as np 

img = np.zeros((512,512,3), dtype=np.uint8)

# Rectangle
cv2.rectangle(img, pt1=(130,130), pt2=(300,300), color=(255,0,0), thickness= 5 )

# Create Circle
cv2.circle(img, center=(100,400), radius=50, color=(0,0,255), thickness= -1)

#Line
cv2.line(img, pt1=(0,0), pt2=(512,512), thickness=2, color=(0,255,0))

# Text

cv2.putText(
    img, 
    text="Mehedi", 
    org=(80, 90), 
    fontFace=cv2.FONT_ITALIC, 
    fontScale=4, 
    color=(255, 50, 255), 
    thickness=1, 
    lineType=cv2.LINE_AA
)
cv2.imshow("Create Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
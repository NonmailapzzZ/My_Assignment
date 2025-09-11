import cv2
import numpy as np
import matplotlib.pyplot as plt


#include a parameter
img_path = r' ~IMAGE PATH '
upper_blue = 110
lower_blue = 96.7

# read image from picture input
image = cv2.imread(img_path)
man = image.copy()

# blurred image by using guassianblur
blur = cv2.GaussianBlur(image,(5,5),0)

# convert from RGB to HSV
blur = cv2.cvtColor(blur, cv2.COLOR_BGR2LAB)

_,_, B = cv2.split(blur)

# inv-threshold a blue color in picture
_, frame = cv2.threshold(B, lower_blue, 255, cv2.THRESH_BINARY)
con, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# mask an image from threshold
res = cv2.bitwise_and(image, image, mask=frame)
result = res.copy()
cv2.drawContours(result, con, -1, (0,0,255), 2)

cv2.imshow("Threshold with contour",result)
cv2.waitKey(0)
cv2.destroyAllWindows()

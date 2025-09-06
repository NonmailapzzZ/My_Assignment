import argparse    # import argparse module 
import numpy as np # import Numpy module.
import cv2         # import OpenCV module.
# "imread" : read the image files using file name
Outdoor = cv2.imread('Figures/Cube1.jpg')
Indoor = cv2.imread('Figures/Cube8.jpg')
# "cvtColor": convert image from one color space to another color space
OutdoorHSV = cv2.???(Outdoor, cv2.???)
IndoorHSV = cv2.???(Indoor, cv2.???)
cv2.imshow("Outdoor", Outdoor)
cv2.imshow("Indoor", Indoor)

(Ho, So, Vo) = cv2.???(OutdoorHSV)
HSVspaceo = np.hstack([Ho,So,Vo])
cv2.imshow("HSV space: Outdoor", HSVspaceo)

(Hi, Si, Vi) = cv2.???(IndoorHSV)
HSVspacei = np.hstack([Hi,Si,Vi])
cv2.imshow("HSV space: Indoor", HSVspacei)

cv2.waitKey(0)
cv2.destroyAllWindows()

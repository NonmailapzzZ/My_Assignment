import argparse    # import argparse module 
import numpy as np # import Numpy module.
import cv2         # import OpenCV module.
# "imread": read the image files using file name
Outdoor = cv2.imread('Figures/Cube1.jpg')
Indoor = cv2.imread('Figures/Cube8.jpg')
# "cvtColor": convert image from one color space to another color space
OutdoorLab = cv2.???(Outdoor, cv2.???)
IndoorLab = cv2.???(Indoor, cv2.???)

cv2.imshow("Outdoor", Outdoor)
cv2.imshow("Indoor", Indoor)

# "split" to unpack the image into 3 channels in (L, a, b) order.
# Each channel is represented as a ndarray with 2 dimensions.
(Lo, ao, bo) = cv2.???(OutdoorLab)
# "hstack" to stack array (R,G,B matrices) horizontally.
Labspaceo = np.hstack([Lo,ao,bo])
cv2.imshow("Lab-space: Outdoor", Labspaceo)

# "split" to unpack the image into 3 channels in (L, a, b) order.
# Each channel is represented as a ndarray with 2 dimensions.
(Li, ai, bi) = cv2.???(IndoorLab)
# "hstack" to stack array (R,G,B matrices) horizontally.
Labspacei = np.hstack([Li,ai,bi])
cv2.imshow("Lab space: Indoor", Labspacei)

cv2.waitKey(0)
cv2.destroyAllWindows()
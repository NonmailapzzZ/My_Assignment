import argparse    # import argparse module 
import numpy as np # import Numpy module.
import cv2         # import OpenCV module.
# "imread" : read the image files using file name
Outdoor = cv2.imread('Figures/Cube1.jpg')
Indoor = cv2.imread('Figures/Cube8.jpg')

cv2.imshow("Outdoor Cube Image", Outdoor)
cv2.imshow("Indoor Cube Image", Indoor)

# "split" to unpack the image into 3 channels in (B, G, R) order.
# Each channel is represented as a ndarray with 2 dimensions.
(Bo, Go, Ro) = cv2.???(Outdoor)
# "hstack" to stack array (R,G,B matrices) horizontally.
BGRspaceo = np.???([???,???,???])
cv2.imshow("BGR space: Outdoor", BGRspaceo)

# "split" to unpack the image into 3 channels in (B, G, R) order.
(Bi, Gi, Ri) = cv2.???(Indoor)
# "hstack" to stack array (R,G,B matrices) horizontally.
BGRspacei = np.???([???,???,???])
cv2.imshow("BGR space: Indoor", BGRspacei)

cv2.waitKey(0)
cv2.destroyAllWindows()


import argparse    # import argparse module 
import numpy as np # import Numpy module.
import cv2         # import OpenCV module.

# "ArgumentParser" is creating an object to parse the command line
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args = vars(ap.parse_args())
# "imread" : read the image file using "args" variable
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# "GaussianBlue" to smooth image with Kernel Size = 5x5
blurred = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Gaussian Blur", blurred)

# "threshold" to segment image with illumination above 210 to 255 to select white background area
(T, thresh) = cv2.???(blurred, ???, ???, cv2.???)
cv2.imshow("Threshold Binary", thresh)

# "threshold" to segment image with illumination below 210 to select coins area
(T, threshINV) = cv2.???(blurred, ???, ???, cv2.???)
cv2.imshow("Threshold Binary Inverse", threshINV)

# "bitwise_and" calculates the per-element bit-wise conjunction of 2 arrays
cv2.imshow("Paper", cv2.???(image, image, mask = threshINV))
# "waitKey(0) displays image for infinite time until Esc key is pressed.
cv2.waitKey(0)
# "destroyAllWindows" for closing all windows 
cv2.destroyAllWindows()

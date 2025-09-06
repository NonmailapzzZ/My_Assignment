import argparse # import argparse module to write user-friendly command-line interfaces.
import cv2      # import OpenCV module.

# "ArgumentParser" is creating an object to parse the command line into Python data.
ap = argparse.ArgumentParser()
# "add_argument" to take the strings on the command line and turn them into objects.
ap.add_argument("-i","--image",required=True)
args = vars(ap.parse_args())

# "imread" : read the image file using "args" variable
image = cv2.imread(args["image"])
cv2.imshow("Original Image", image) # display "image" in window 1

# Select sliced-matrix image along
# height[190:320] = 130pixel and width[200:370] = 170pixel
corner = image[190:320,200:370]
cv2.imshow("T-Letter Image", corner) # display "T-letter" in window 2

# Assign above sliced-matrix image with red color
image[190:320, 200:370] = (0,255,0      )

# "imshow" display modified "image" in window 3
cv2.imshow("Modify Image", image)
# "waitKey(0) displays image for infinite time until Esc key is pressed.
cv2.waitKey(0)
# "destroyAllWindows" for closing only 'SnapshotTest' window 
cv2.destroyWindow('Inputed Image')

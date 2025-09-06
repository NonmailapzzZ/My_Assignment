import argparse # import argparse module to write user-friendly command-line interfaces.
import cv2      # import OpenCV module

# "ArgumentParser" is creating an object to parse the command line into Python data.
ap = argparse.ArgumentParser(description='Load Image.')
# "add_argument" to take the strings on the command line and turn them into objects.
ap.add_argument("-i","--image",required=True,
                help='path to an input-image file')
args = vars(ap.parse_args())

# "imread" : read the image file using "args" variable
image = cv2.imread(args["image"])
# "image.shape" : show dimension of image object 
print("width: %d pixels" % (image.shape[1])) 
print("height: %d pixels" % (image.shape[0]))
print("channels: %d" % (image.shape[2])) 

# "imshow" display "frame" in window 
cv2.imshow("Inputed Image", image)
# "waitKey(0) displays image for infinite time until Esc key is pressed.
cv2.waitKey(0)
# "destroyAllWindows" for closing only 'SnapshotTest' window 
cv2.destroyWindow('Inputed Image')

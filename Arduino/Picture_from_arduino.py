import cv2
from urllib.request import urlopen
import numpy as np
import time

url = r'http://10.88.88.217/capture'
while True :
    img_resp = urlopen(url)
    img_np = np.asarray(bytearray(img_resp.read()),dtype="uint8")
    img = cv2.imdecode(img_np, -1)
    img = cv2.imshow("Camera",img)
    time.sleep(1)
    if ord('q') == cv2.waitKey(10):
        exit(0)

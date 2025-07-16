import cv2
import numpy as np
img = cv2.imread("C:/Users/harsh/OneDrive/Desktop/COMPUTER VISION/cv.jpeg", 0)
if img is None:
    exit()
sx = cv2.Sobel(img, cv2.CV_64F, 1, 0, 3)
sy = cv2.Sobel(img, cv2.CV_64F, 0, 1, 3)
mag = cv2.normalize(np.sqrt(sx**2 + sy**2), None, 0, 255, cv2.NORM_MINMAX)
cv2.imshow("Boundary", np.uint8(mag))
cv2.waitKey(0)
cv2.destroyAllWindows()

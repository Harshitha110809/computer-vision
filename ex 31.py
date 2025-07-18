import cv2
import numpy as np
image = cv2.imread("C:/Users/harsh/OneDrive/Desktop/COMPUTER VISION/cv.jpg", cv2.IMREAD_GRAYSCALE)
if image is not None:
    kernel = np.ones((5, 5), np.uint8)
    opening_result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Original Image", image)
    cv2.imshow("Opening Result", opening_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load the image.")


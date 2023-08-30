import cv2 as cv
import numpy as np

rectangle = np.zeros((512, 512, 3), np.uint8) + 255

cv.rectangle(rectangle, (50, 50), (200, 200), (0, 0, 255), 0)
cv.imshow("Dikdortgen", rectangle)

cv.waitKey(0)
cv.destroyAllWindows()


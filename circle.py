import cv2 as cv
import numpy as np

circle = np.zeros((512, 512, 3), np.uint8) + 255

cv.circle(circle, (256, 256), 60, (255, 0, 0), -1) # -1 => İçi dolu oldu.

cv.imshow("Cember", circle)

cv.waitKey(0)
cv.destroyAllWindows()

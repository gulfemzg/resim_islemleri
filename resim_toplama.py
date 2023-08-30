import cv2 as cv
import numpy as np

circle = np.zeros((512, 512, 3), np.uint8) + 255
rectangle = np.zeros((512, 512, 3), np.uint8) + 255

cv.circle(circle, (256, 256), 50, (255, 0, 0), -1)
cv.rectangle(rectangle, (250, 250), (300, 300), (0, 0, 255), -1)


add = cv.add(circle, rectangle)

cv.imshow("Circe", circle)
cv.imshow("Rectangle", rectangle)
cv.imshow("Added", add)


cv.waitKey(0)
cv.destroyAllWindows()


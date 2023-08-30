# Dosya yolu girilen resmi siyah beyaza çevirme.

import cv2

dosya_yolu = input("Resmin dosya yolunu giriniz : ")

image = cv2.imread(dosya_yolu, 0)
original = cv2.imread(dosya_yolu)

cv2.imshow("Siyah Beyaz", image)
cv2.imshow("Orijinal", original)

cv2.waitKey(0)
cv2.destroyAllWindows()

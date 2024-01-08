import cv2
import matplotlib.pyplot as plt

img = cv2.imread("R.jpg",0)
ret,th = cv2.threshold(img,125,255,cv2.THRESH_BINARY)
plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2_imshow("gray",img)
cv2_imshow("threshold",img)

cv2.waitkey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

#drawing image
img=np.zeros((400,400,3))
cv2.line(img, (50, 160), (100, 160), (0, 213, 255), 5)
cv2.rectangle(img, (30, 30), (300, 200), (200, 255, 0), 2)
cv2.circle(img, (200, 200), 80, (255, 0, 215), 2)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Debanwita Ghosh', (30, 30),
            font, 1, (0, 255, 100), 2, cv2.LINE_AA)
cv2.imshow('window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


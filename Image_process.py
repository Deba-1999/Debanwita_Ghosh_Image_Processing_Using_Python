import cv2
import numpy as np
img=cv2.imread("moon.png")
#cv2.imshow('Original', img)
#print(type(img))
#print(img.shape)
#imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#imgBlur=cv2.GaussianBlur(imgGray,(15,15),0)
#cv2.imshow("gray_image",imgGray)
#cv2.imshow("blur_image",imgBlur)
#imgBlue=img[:,:,0]
#imgGreen=img[:,:,1]
#imgRed=img[:,:,2]
#newImg=np.hstack((imgBlue,imgGreen,imgRed))
#cv2.imshow("merge_image",newImg)
#img[:,:,2]=0
#cv2.imshow("Red_off",img)
#img_resize=cv2.resize(img,(256,256))
#cv2.imshow("resize",img_resize)
#Flip
#img_flip=cv2.flip(img,0) #vertical
#cv2.imshow("moon_1",img_flip)

#img_flip2=cv2.flip(img,1) #horizontal
#cv2.imshow("moon_2",img_flip2)

#img_flip3=cv2.flip(img,-1) #both
#cv2.imshow("moon_3",img_flip3)
#img_crop=img[100:200,300:400]
#cv2.imshow("crop",img_crop)

cv2.waitKey(0)
#cv2.imwrite("Moon_crop.png",img_crop)

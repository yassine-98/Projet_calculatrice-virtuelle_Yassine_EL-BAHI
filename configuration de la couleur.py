import cv2 as cv
import numpy as np


def vide(a):
    pass

cap = cv.VideoCapture(0)
cap.set(3,800)
cap.set(4,650)
cv.namedWindow('Paint')
cv.resizeWindow('Paint',300,300)

cv.createTrackbar('H_max','Paint',179,179,vide)
cv.createTrackbar('H_min','Paint',0,179,vide)
cv.createTrackbar('S_max','Paint',255,255,vide)
cv.createTrackbar('S_min','Paint',0,255,vide)
cv.createTrackbar('V_max','Paint',255,255,vide)
cv.createTrackbar('V_min','Paint',0,255,vide)


while True:
    test,img = cap.read()
    if not test:
        break

    img = cv.flip(img,1)
    img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    u_h = cv.getTrackbarPos('H_max', 'Paint')
    u_s = cv.getTrackbarPos('S_max', 'Paint')
    u_v = cv.getTrackbarPos('V_max', 'Paint')
    l_h = cv.getTrackbarPos('H_min', 'Paint')
    l_s = cv.getTrackbarPos('S_min', 'Paint')
    l_v = cv.getTrackbarPos('V_min', 'Paint')

    lower_range = np.array([l_h,l_s,l_v])
    upper_range = np.array([u_h,u_s,u_v])

    mask = cv.inRange(img_hsv,lower_range,upper_range)
    img_bit = cv.bitwise_and(img,img, mask = mask)

    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)

    img_result = np.hstack((img_bit,img,mask))
    img_result = cv.resize(img_result,None,fx=0.6,fy=0.8)

    cv.imshow('Paint',img_result)

    key = cv.waitKey(1)

    if key == 27:
        break

    if key == ord('s'):
        HSV = [[l_h,l_s,l_v], [u_h,u_s,u_v]]
        print(HSV)
        np.save('Color_val',HSV)
        break
cap.release()
cv.destroyAllWindows()
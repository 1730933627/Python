import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cap = cv.VideoCapture(0)
one = np.ones((2,2),np.uint8)

word = cv.imread("img/word.jpg",0)
h,w = word.shape


while 1:
    ret,img = cap.read()
    gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    res = cv.matchTemplate(gray_img, word, cv.TM_CCORR)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print(min_val,"\t",max_val,"\t",min_loc,'\t',max_loc)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    if max_val > 3750000000:
        img_p = cv.rectangle(gray_img, top_left, bottom_right, (255, 255, 255), 2)
        cv.imshow('cap',img_p)
    else:
        cv.imshow('cap',gray_img)
    # th = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)

    cv.moveWindow('cap',500,200)
    if cv.waitKey(1) & 0xFF == ord('q'):
        # cv.imwrite('img/word.jpg',gray_img)
        break

cap.release()
cv.destroyAllWindows()

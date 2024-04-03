import cv2
import numpy as np

image = cv2.imread('Resources\input_image.png')
imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blank = np.zeros(image.shape, dtype='uint8')
ret, thresh = cv2.threshold(imgray, 255, 255, cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(thresh, 
          cv2.RETR_LIST,   cv2.CHAIN_APPROX_NONE)

# drawing contours
cv2.drawContours(blank, contours, -1, (0, 0, 255), 1)


# contors area
sum =0
for i in range (len(contours)):
    sum += cv2.contourArea(contours[i])

# print(sum)

RATIO_PIXEL_TO_CM = 78 # 78 pixels are 1cm
RATIO_PIXEL_TO_SQUARE_CM = 78 * 78
area_cm = round(sum / RATIO_PIXEL_TO_SQUARE_CM, 2)
print("Area in cm bse on ratio of Pixel to Square cm is {} cm*2".format(area_cm))

# resizing image

# x,y,z =image.shape
# x=x//2
# y=y//2
# image = cv2.resize(image,(y,x))
# blank = cv2.resize(blank,(y,x))
# thresh = cv2.resize(thresh,(y,x))


#printing image

# cv2.imshow('image', image)
# cv2.imshow('contours', blank)
# cv2.imshow('threshold', thresh)
# cv2.waitKey(0)


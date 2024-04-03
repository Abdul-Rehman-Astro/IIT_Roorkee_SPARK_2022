import cv2

image = cv2.imread("input.tif", -1)

img_scaled = cv2.normalize(image, dst=None, alpha=0, beta=65535, norm_type=cv2.NORM_MINMAX)
cv2.imshow('tiff', img_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(image)
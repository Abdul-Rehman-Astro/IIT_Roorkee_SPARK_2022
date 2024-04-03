import numpy as np
import matplotlib.pyplot as plt
import cv2

from matplotlib.pyplot import figure
from PIL import Image


# img_path = "Label.tif"

img_path = "Label1.jpg"

# Reading image 
img = cv2.imread(img_path)
im1 = np.array(img)
figure(figsize=(20, 15), dpi=80)
plt.imshow(im1)
plt.show()

# arr = np.array(img)


# to print all arrays of this image 
# np.set_printoptions(threshold=np.inf)



# printing all labesl array 
# print(arr)


# histogram of image

histg = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histg)
plt.title("Labels")
plt.show()
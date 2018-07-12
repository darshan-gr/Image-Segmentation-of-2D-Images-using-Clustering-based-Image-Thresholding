import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load the input image.
img = cv2.imread('../data/cars.jpg') # ImageSegmentation/DataInput/coins.jpg

# Convert image to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Display input image
plt.imshow(gray, 'gray')
plt.title('Input')
plt.show()

# Threshold using the opencv module, using otsus thresholding.
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Save the output image
cv2.imwrite("../result/cars_thresh.jpg", thresh)

plt.imshow(thresh, 'gray')
plt.title('Output')
plt.show()

import numpy as np
import cv2
from matplotlib import pyplot as plt

imag = cv2.imread('../data/cars.jpg',0)
blurred = cv2.GaussianBlur(imag,(5,5),0)

plt.imshow(blurred, 'gray')
plt.title('Input')
plt.show()

# find normalized_histogram, and its cumulative distribution function
# Returns 256*1 numpy matrix, each having the number of pixels with that value of intensity
histogram = cv2.calcHist([blurred],[0],None,[256],[0,256])

# Plot the normalized histogram
plt.hist(histogram, np.arange(256))
img = plt.gcf()
plt.show()
img.savefig('../result/cars4_hist.png', dpi=100)

# print hist.shape
# print hist.max()

# Normalize this histogram from 0 to 1
hist_normalize = histogram.ravel()/histogram.max()

# print hist_norm.shape

# Find the cumulative distribution of the pixels wrt intensity
Q = hist_normalize.cumsum()
# print Q.shape

x_axis = np.arange(256)
mini = np.inf
thresh = -1
for i in range(1,256):
    # probabilities
    p1,p2 = np.hsplit(hist_normalize,[i])

    # cumulative sum of classes
    q1,q2 = Q[i],Q[255]-Q[i]

    # weights
    b1,b2 = np.hsplit(x_axis,[i])

    # finding means and variances
    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2

    # calculates the minimization function
    fn = v1*q1 + v2*q2
    if fn < mini:
        mini = fn
        thresh = i

# find otsu's threshold value with OpenCV function
ret, binarized = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Save the output image
cv2.imwrite("../result/cars4_thresh.jpg", binarized)

plt.imshow(binarized, 'gray')
plt.title('Output')
plt.show()

print ("Threshold gotten by native implementation:",thresh)
print ("Threshold gotten by the OpenCV implementation:",ret)

print ("Percentage error in calculation is",abs(thresh-ret)/ret*100.0,"%")

# Image-Segmentation-of-2D-Images-using-Clustering-based-Image-Thresholding

**Image Segmentation into foreground and background using OTSU method** 


**Steps used in OTSU Algorithm:**
1. Compute the histogram of pixel intensities vs the number of pixels
2. Loop through the grayscale intensities from 0 to 255, setting each as a threshold
3. Compute the weighted mean, and the variance from the function
4. Compute the function value at that point
5. Update minimum variance and then update the threshold

-----------
**Example implementation**
The input image is:-<br/><br/>
![Input Image](/data/cars4.bmp)
<br/>
The histogram for the given image is:-<br/><br/>
![Histogram](/result/cars4_hist.png)
<br/>
The output of the binarization is:-<br/><br/>
![Output](/result/cars4_thresh.jpg)
<br/><br/>

**Dependencies**

- Python36
- OTSU Threshold
- OpenCV
- Matplotlib
- Numpy

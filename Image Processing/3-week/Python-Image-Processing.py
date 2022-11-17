#-----------------------------------------------------------------------------------------------------------------------------------------------     
# Python Image Processing
#--------------------------------------------------------------------------------------------------------------
import cv2
import numpy as np

image1 = cv2.imread("brain.jpg")

cv2.imshow("Brain", image1)

# To see the size of the picture
print(image1.size)

# To see the data type of the image
print(image1.dtype)


# To find out the width, height and muscle channel of the picture
print(image1.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
# ------------------------------------------------------------------------------------------------------------------------------------------------

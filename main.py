import skimage
from skimage import exposure, img_as_float
import cv2
import glob
import os

filepath = glob.glob('C:/Users/ngoth/Documents/UMKC/Gamma Correction/NWPU-RESISC45/NWPU-RESISC45/airplane/*.jpg')

i=0
for file in filepath:
    print(file)
    img = cv2.imread(file)
    image = img_as_float(img)
    gamma_corrected = exposure.adjust_gamma(image, 7)

    cv2.imwrite("C:/Users/ngoth/Documents/UMKC/Gamma Correction/Gamma_NWPU-RESISC45/Gamma_Airplane/gamma_airplane%i" %i, gamma_corrected)
    cv2.imshow('image', gamma_corrected)
    # Maintain output window until user presses a key
    cv2.waitKey(300)

    # Destroying present windows on screen
    cv2.destroyAllWindows()


"""
img = cv2.imread("C:/Users/ngoth/Documents/UMKC/Gamma Correction/IMG01.jpg")
image = img_as_float(img)
gamma_corrected = exposure.adjust_gamma(image,7)

cv2.imshow('image', gamma_corrected)

# Maintain output window utill
# user presses a key
cv2.waitKey(0)

# Destroying present windows on screen
cv2.destroyAllWindows()
"""

"""
for filename in os.listdir(filepath):
    if filename.endswith(".jpg"):
        img = cv2.imread(filename)
        image = img_as_float(img)
        gamma_corrected = exposure.adjust_gamma(image, 7)
        cv2.imshow('image', gamma_corrected)

        # Maintain output window utill
        # user presses a key
        cv2.waitKey(0)

        # Destroying present windows on screen
        cv2.destroyAllWindows()
"""

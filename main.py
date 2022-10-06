import skimage
from skimage import exposure, img_as_float
from math import log10, sqrt
import numpy as np
import cv2
import glob
import os

# filepath = "C:/Users/ngoth/Documents/UMKC/Gamma Correction/NWPU-RESISC45/NWPU-RESISC45/wetland"
# pathfile = 'C:/Users/ngoth/Documents/UMKC/Gamma Correction/Gamma_NWPU-RESISC45/Gamma_Airplane'

filepath = "C:/Users/ngoth/Documents/UMKC/NWPU-RESISC45/NWPU-RESISC45/airplane"
files = os.listdir(filepath)
# print(files)
# paths = os.listdir(pathfile)

# def PSNR(original, compressed):
#     mse = np.mean((original - compressed) ** 2)
#     if (mse == 0):  # MSE is zero means no noise is present in the signal .
#         # Therefore PSNR have no importance.
#         return 100
#     max_pixel = 255.0
#     psnr = 20 * log10(max_pixel / sqrt(mse))
#     return psnr


for file in files:
    img_path = os.path.join(filepath, file)
    img = cv2.imread(img_path)
    image = img_as_float(img)
    gamma_corrected = exposure.adjust_gamma(image, 4)
    result = cv2.normalize(gamma_corrected, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # cv2.imshow('image', gamma_corrected)
    cv2.imwrite(f"C:/Users/ngoth/Documents/UMKC/Gamma_NWPU-RESISC45/Gamma_airplane/gamma_{file}", result)
    # Maintain output window until user presses a key
    # cv2.waitKey(300)

    # Destroying present windows on screen
    # cv2.destroyAllWindows()

# values = []
# files_list = []
# paths_list = []
# for file in files:
#     img_path = os.path.join(filepath, file)
#     files_list.append(img_path)
#
# for path in paths:
#     path_img = os.path.join(pathfile,path)
#     paths_list.append(path_img)
#
# for imgpath, pathimg in zip(files_list, paths_list):
#     img = cv2.imread(imgpath)
#     img1 = cv2.imread(pathimg)
#     value = PSNR(img, img1)
#     values.append(values)
#     #print(f"PSNR value is {value} dB")
#     np.savetxt('C:/Users/ngoth/Documents/UMKC/Gamma Correction/PSNR/PSNR_airplane.txt', values)

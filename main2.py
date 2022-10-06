import skimage
from skimage import exposure, img_as_float
from math import log10, sqrt
import numpy as np
import cv2
import glob
import os

filepath = "C://Users//ngoth//Documents//NWPU-RESISC45"
#pathfile = 'C:/Users/ngoth/Documents/UMKC/Gamma Correction/Gamma_NWPU-RESISC45/Gamma_Airplane'

files = os.listdir(filepath)
print(files)

for file in files:
    img_path = os.path.join(filepath,file)
    pg = "C://Users//ngoth//Documents//Ga"
    dire = os.path.join(pg,file)
    os.mkdir(dire)
    dirs = os.listdir(img_path)
    for dir in dirs:
        dir_path = os.path.join(img_path,dir)
        img = cv2.imread(dir_path)
        image = img_as_float(img)
        gamma_corrected = exposure.adjust_gamma(image, 4)
        result = cv2.normalize(gamma_corrected, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        # cv2.imshow('image', gamma_corrected)
        # path = os.path.join(dire, dirs)
        cv2.imwrite(f"C://Users//ngoth//Documents//Ga//airplane//gamma_{dir}", result)
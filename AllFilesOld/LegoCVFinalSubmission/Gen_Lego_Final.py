"""
python Gen_Lego_Final.py
Generate Lego File
"""

from PIL import Image
import os
from legofy import main as getLego
import cv2
import numpy as np


def convertGrayscale(InputPath, OutputPath):
    image_file = Image.open(InputPath)  # open colour image
    image_file = image_file.convert('1')  # convert image to black and white
    image_file.save(OutputPath)


def applyCLAHE(InputPath, OutputPath, ReshapeSize=None, cliplimit=5, gridsize=(8, 8)):
    image = cv2.imread(InputPath)
    if not ReshapeSize == None:
        image = cv2.resize(image, ReshapeSize)
    image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=cliplimit, tileGridSize=gridsize)
    final_img = clahe.apply(image_bw)  # + 30
    cv2.imwrite(OutputPath, final_img)


if __name__ == '__main__':
    # initial configuration
    ROOT_DIR = os.getcwd()
    ImgPath = os.path.join(ROOT_DIR, "ProblemStatement", "InputImg.jpeg")
    OutputDir = os.path.join(ROOT_DIR, 'GenFinal')
    
    FilterList = [45, 180, 360, 450]
    
    for FilterSize in FilterList:
        OutputPath = os.path.join(OutputDir, "OutAll"+str(FilterSize) + ".jpeg")    
        # Make Legos
        getLego(image_path=ImgPath, output_path=OutputPath,
                size=FilterSize, palette_mode="all", dither=False)
        # Apply Filters
        ImageSizes = [(70,70) , (105,105),(256,256),(512,512),(1024,1024),(2048,2048) ]
        for imgSize in ImageSizes:
            OutputFilterPath = os.path.join(OutputDir, "OutAllFiltered"+str(FilterSize) + "Size"+str(imgSize)+".jpeg")
            applyCLAHE(OutputPath, OutputFilterPath,ReshapeSize=imgSize)

"""
Output Sizes :
4900 pixels (70*70), and 11025 pixels (105*105)
"""

"""
python Gen_Lego.py
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
    OutputDir = os.path.join(ROOT_DIR, 'GenLogos')
    FilterSize = 360 # 180 # 45, 450
    OutputPath = os.path.join(OutputDir, "OutAll"+str(FilterSize) + ".jpeg")
    OutputFilterPath = os.path.join(
        OutputDir, "OutAllFiltered"+str(FilterSize) + ".jpeg")
    
    # Make Legos
    getLego(image_path=ImgPath, output_path=OutputPath,
            size=FilterSize, palette_mode="all", dither=False)
    # convert to GrayScale
    # convertGrayscale(OutputPath, BWOutputPath)
    applyCLAHE(OutputPath, OutputFilterPath)

"""
Output Sizes :
4900 pixels (70*70), and 11025 pixels (105*105)
"""
"""
# Reading the image from the present directory
image = cv2.imread("image.jpg")
# Resizing the image for compatibility
image = cv2.resize(image, (500, 600))

# The initial processing of the image
# image = cv2.medianBlur(image, 3)
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# The declaration of CLAHE
# clipLimit -> Threshold for contrast limiting
clahe = cv2.createCLAHE(clipLimit=5)  # clipLimit=2.0, tileGridSize=(8,8)
final_img = clahe.apply(image_bw) + 30

# Ordinary thresholding the same image
_, ordinary_img = cv2.threshold(image_bw, 155, 255, cv2.THRESH_BINARY)

# Showing all the three images
cv2.imshow("ordinary threshold", ordinary_img)
cv2.imshow("CLAHE image", final_img)
"""

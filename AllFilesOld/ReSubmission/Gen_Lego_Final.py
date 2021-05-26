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
    return final_img

def applyReshape(InputPath, OutputPath, ReshapeSize=None):
    image = cv2.imread(InputPath)
    if not ReshapeSize == None:
        image = cv2.resize(image, ReshapeSize)
    cv2.imwrite(OutputPath, image)
    return image

def DarkenImg2D (arr):
    """
    Given Dark Colours : Taking Means
    233
    164
    91
    45
    21
    """
    return None

def isGreater(tup1,tup2):
    a,b,c  =tup1
    p,q,r = tup2
    
    if a>p and  b>q and c>r:
        return True
    else:
        return False

def DarkenImg3D (arr):
    """
    arr : x*y*3
    Given Dark Colours :
    #e8eae9 : rgb(232,234,233)
    #99a3af : rgb(153,163,175)
    #596570 : rgb(059,101,112)
    #222c3a : rgb(034,044,058)
    #222c3a : rgb(017,022,024)
    
    Given Dark Colours : Taking Means
    233
    164
    91
    45
    21
    """
    Ranges = [(255,255,255) , (232,234,233) , (153,163,175) , (59,101,112) , (34,44,58) ,(17,22,24) , (0,0,0) ]
    Ranges = Ranges[::-1]
    x,y,z = arr.shape
    for i in range(x):
        for j in range(y):
            val = arr[i][j]
            count = 0
            while True:
                new_val = Ranges[count]
                if  isGreater(val, new_val):
                    count += 1
                    continue
                else:
                    new_val = Ranges[count]
                    break
            arr[i][j] = new_val 
    return arr
    
def DarkenImg (arr):
    if len(arr.shape )==2:
        return DarkenImg2D(arr)
    elif len(arr.shape) ==3:
        return DarkenImg3D(arr)
    else:
        return 0

if __name__ == '__main__':
    # initial configuration
    ROOT_DIR = os.getcwd()
    ImgPath = os.path.join(ROOT_DIR, "ProblemStatement", "InputImg.jpeg")
    OutputDir = os.path.join(ROOT_DIR, 'GenFinal')
    
    FilterList = [45, 70, 105, 120, 140, 180, 360, 450]
    
    for FilterSize in FilterList:
        OutputPath = os.path.join(OutputDir, "OutAll"+str(FilterSize) + ".jpeg") 
        OutputPathDithered = os.path.join(OutputDir, "OutAll"+str(FilterSize) + "_dit.jpeg") 
        # Make Legos
        getLego(image_path=ImgPath, output_path=OutputPath,
                size=FilterSize, palette_mode="custom2", dither=False)
        
        getLego(image_path=ImgPath, output_path=OutputPathDithered,
                size=FilterSize, palette_mode="custom2", dither=True)
        # Apply Filters
        ImageSizes = [(70,70) , (105,105),(256,256),(512,512),(1024,1024),(2048,2048) ]
        # ImageSizes = ImageSizes[::-1]
        for imgSize in ImageSizes:
            OutputFilterPath = os.path.join(OutputDir, "OutAllFiltered"+str(FilterSize) + "Size"+str(imgSize)+".jpeg")
            # OutputDarkFilterPath = os.path.join(OutputDir, "OutAllFiltered"+str(FilterSize) + "Size"+str(imgSize)+"_Dark.jpeg")
            OutputReshapePath = os.path.join(OutputDir, "OutAllReshape"+str(FilterSize) + "Size"+str(imgSize)+".jpeg")
            
            """
            image = cv2.imread(OutputPath)
            # print(image)
            # print(image.shape)
            arr = DarkenImg(image)
            cv2.imwrite(OutputDarkFilterPath, arr)
            """
            reshape_img = applyReshape(OutputPath, OutputReshapePath,ReshapeSize=imgSize)
            filter_img = applyCLAHE(OutputPath, OutputFilterPath,ReshapeSize=imgSize)
            # print("Shape :",filter_img.shape)
            # print("Max :",np.max(filter_img),"Min :",np.min(filter_img))
            # np.savetxt(os.path.join(OutputDir, "FinalImg"+str(FilterSize) + "Size"+str(imgSize)+".csv"), filter_img, delimiter=',')
"""
Output Sizes :
4900 pixels (70*70), and 11025 pixels (105*105)
"""

import os
import cv2
import numpy as np
from PIL import Image

img = Image.open("/home/pi/project/potatodatasets/image1.jpg")#input image that is clicked by camera
# This would print all the files and directories

img1=img.crop((0,0,1300,2000))
img1.save("/home/pi/project/cropped_images/imagename.jpg")

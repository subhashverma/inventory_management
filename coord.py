import cv2
import numpy as np
from PIL import Image

im=cv2.imread('image1.jpg',0)
img = Image.open("image2.jpg")

pixels=np.argwhere(im != 255)
sum1,sum2,min_x,max_x,min_y,max_y = 0,0,4000,0,4000,0
for i,j in pixels:
	sum1+=i
	sum2+=j
	if(min_x>i):
		min_x=i
	if(max_x<i):
		max_x=i
	if(min_y>j):
		min_y=j
	if(max_y<j):
		max_y=j
	#print(i,",",j)
print()
n=len(pixels)
print("min_x=",min_x,", max_x=",max_x,", min_y=",min_y,", max_y=",max_y)
a,b=round(sum1/n),round(sum2/n)
print(a,b)
img1=img.crop((min_x,min_y,max_x,max_y))
img1.save("/home/pi/project/cropped_images/img1.jpg")


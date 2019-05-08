import os
import cv2
import numpy as np
from PIL import Image
path = "/home/pi/project/output-images/"
dirs = os.listdir( path )
count =1
dic1={}

#img = Image.open("/home/pi/project/potatodatasets/image1.jpg")#input image that is clicked by camera
# This would print all the files and directories

for imagename in dirs:	
	img = Image.open("/home/pi/project/potatodatasets/image1.jpg")
	print("image number processing")
	print(count)
	print(imagename)
	count+=1
	im=cv2.imread(path+imagename,0)
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
	print("min_x =",min_x,", max_x =",max_x,", min_y =",min_y,", max_y =",max_y)
	a,b=round(sum1/n),round(sum2/n)
	dic1.update({imagename:[a,b]})
	print(a,b)
	img1=img.crop((min_y,min_x,max_y,max_x))
	img1.save("/home/pi/project/cropped_images/"+imagename)
print(dic1)

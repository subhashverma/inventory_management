import cv2
import os, sys
from keras.models import load_model

IMAGE_SIZE= 200
model=load_model('potmodel.h5')
path = "/home/pi/project/cropped_images/"
dirs = os.listdir( path )
count =1
# This would print all the files and directories
for imagename in dirs:
	#file=file.split(".")i
	#if(len(file)==2 and file[1]=="jpg"):
	print("image number processing")
	print(count)
	print(imagename)
	count+=1
	img = cv2.imread(path+imagename)
	img = cv2.resize(img,(IMAGE_SIZE,IMAGE_SIZE))
	img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
	m=model.predict([img])[0]
	print(m)
	if(m[0]>m[1]):
		print("potato\n")
	elif(m[0]<m[1]):
		print("weed\n")

#!/usr/bin/python
import os, sys
import weedpotato as pre
import cv2
import numpy as np
import lcd_i2c
from PIL import Image

# Open a file
lcd_i2c.main(string1="Image Captured",string2 = "")
path = "/home/pi/project/potatodatasets/"
dirs = os.listdir( path )
# This would print all the files and directories
for imagename in dirs:	
	print("image processing")
	print(imagename)
	pre.main(path,imagename)
lcd_i2c.main(string1="Preprocessing",string2 = "Image")
# Open a file
path = "/home/pi/project/output-images/"
dirs = os.listdir( path )
count =1
dic1={}

# This would print all the files and directories
lcd_i2c.main(string1="Finding ",string2 = "Weed Coordinates")
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

from keras.models import load_model
#image classification using ml model
IMAGE_SIZE= 200
model=load_model('potmodel.h5')
path = "/home/pi/project/cropped_images/"
dirs = os.listdir( path )
count =1
# This would print all the files and directories
l=[]
lcd_i2c.main(string1="Classification",string2 = "In Progress")
for imagename in dirs:
	print("image number processing")
	print(count)
	print(imagename)
	count+=1
	img = cv2.imread(path+imagename)
	img = cv2.resize(img,(IMAGE_SIZE,IMAGE_SIZE))
	img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
	m=model.predict([img])[0]
	print(m)
	if(m[0]<m[1]):
		print("potato\n")
	elif(m[0]>m[1]):
		print("weed\n")
		for key in dic1.keys():
			if(key == imagename):
				l.append(dic1[key])

print(l)

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

def x_front_y_front(x,y):
	if(x>y):
		GPIO.output(27,GPIO.HIGH)
		GPIO.output(22,GPIO.HIGH)
		if(y>10)
			GPIO.output(6,GPIO.HIGH)
			time.sleep(10)
			GPIO.output(6,GPIO.LOW)
			print("wait sec",y)
			time.sleep(y-10)
		elif(y<10)
			GPIO.output(6,GPIO.HIGH)
			time.sleep(10)
			GPIO.output(6,GPIO.LOW)
			print("wait sec",y)
			time.sleep(y-10)
		GPIO.output(22,GPIO.LOW)
		x=x-y
		print("wait sec",x)
		time.sleep(x)
		GPIO.output(27,GPIO.LOW)
	elif(x<y):
		GPIO.output(27,GPIO.HIGH)
		GPIO.output(22,GPIO.HIGH)
		print("wait sec",x)
		time.sleep(x)
		GPIO.output(27,GPIO.LOW)
		y=y-x
		print("wait sec",y)
		time.sleep(y)
		GPIO.output(22,GPIO.LOW)
	elif(x==y):
		GPIO.output(27,GPIO.HIGH)
		GPIO.output(22,GPIO.HIGH)
		print("wait sec",x)
		time.sleep(y)
		GPIO.output(27,GPIO.LOW)
		GPIO.output(22,GPIO.LOW)
	lcd_i2c.main(string1="Weed removed",string2 = "")
	
def x_back_y_back(x,y):
	if(x>y):
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(23,GPIO.HIGH)
		print("wait sec",y)
		time.sleep(y)
		GPIO.output(23,GPIO.LOW)
		x=x-y
		print("wait sec",x)
		time.sleep(x)
		GPIO.output(17,GPIO.LOW)
	elif(x<y):
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(23,GPIO.HIGH)
		print("wait sec",x)
		time.sleep(x)
		GPIO.output(17,GPIO.LOW)
		y=y-x
		print("wait sec",y)
		time.sleep(y)
		GPIO.output(23,GPIO.LOW)
	elif(x==y):
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(23,GPIO.HIGH)
		print("wait sec",x)
		time.sleep(y)
		GPIO.output(17,GPIO.LOW)
		GPIO.output(23,GPIO.LOW)
	lcd_i2c.main(string1="Weed removed",string2 = "")

def x_back_y_front(x,y):
	if(x>y):
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(22,GPIO.HIGH)
		print("wait sec",y)
		time.sleep(y)
		GPIO.output(22,GPIO.LOW)
		x=x-y
		print("wait sec",x)
		time.sleep(x)
		GPIO.output(17,GPIO.LOW)
	elif(x<y):
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(22,GPIO.HIGH)
		print("wait sec",x)
		time.sleep(x)
		GPIO.output(17,GPIO.LOW)
		y=y-x
		print("wait sec",y)
		time.sleep(y)
		GPIO.output(22,GPIO.LOW)
	elif(x==y):
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(22,GPIO.HIGH)
		print("wait sec",x)
		time.sleep(y)
		GPIO.output(17,GPIO.LOW)
		GPIO.output(22,GPIO.LOW)
	lcd_i2c.main(string1="Weed removed",string2 = "")

def x_front_y_back(x,y):
	if(x>y):
		GPIO.output(27,GPIO.HIGH)
		GPIO.output(23,GPIO.HIGH)
		print("wait sec",y)
		time.sleep(y)
		GPIO.output(23,GPIO.LOW)
		x=x-y
		print("wait sec",x)
		time.sleep(x)
		GPIO.output(27,GPIO.LOW)
	elif(x<y):
		GPIO.output(27,GPIO.HIGH)
		GPIO.output(23,GPIO.HIGH)
		print("wait sec",x)
		time.sleep(x)
		GPIO.output(27,GPIO.LOW)
		y=y-x
		print("wait sec",y)
		time.sleep(y)
		GPIO.output(23,GPIO.LOW)
	elif(x==y):
		GPIO.output(27,GPIO.HIGH)
		GPIO.output(23,GPIO.HIGH)
		print("wait sec",x)
		time.sleep(y)
		GPIO.output(27,GPIO.LOW)
		GPIO.output(23,GPIO.LOW)
	lcd_i2c.main(string1="Weed removed",string2 = "")

x,y=0,0
lcd_i2c.main(string1="Traversing to",string2 = "weed location")
for i,j in l:
	
	i=i*(35/2000)
	j=j*(29/4000)
	if((i>x)&(j>y)):
		a=i-x
		b=j-y
		print(a,b)
		x_front_y_front(a,b)
		time.sleep(3)
	elif((i<x)&(j<y)):
		a=x-i
		b=y-j
		print(a,b)
		x_back_y_back(a,b)
		time.sleep(3)
	elif((i<x)&(j>y)):
		a=x-i
		b=j-y
		print(a,b)
		x_back_y_front(a,b)
		time.sleep(3)
	elif((i>x)&(j<y)):
		a=i-x
		b=y-j
		print(a,b)
		x_front_y_back(a,b)
		time.sleep(3)
	lcd_i2c.main(string1="Moving to next",string2 = "weed location")
	x=i
	y=j
x_back_y_back(x,y)
GPIO.cleanup()
lcd_i2c.main(string1="Traversing to",string2 = "Next Location")


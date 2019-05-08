import os 
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

l=[[1156.0, 2828.0], [1143.0, 424.0], [1151.0, 3613.0], [1146.0, 1228.0], [1151.0, 2031.0]]

def x_front_y_front(x,y):
	if(x>y):
		GPIO.output(27,GPIO.HIGH)
		GPIO.output(22,GPIO.HIGH)
		print("wait sec",y)
		time.sleep(y)
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

x,y=0,0

for i,j in l:
	i=i*(35/2000)
	j=j*(29/4000)
	if((i>x)&(j>y)):
		a=i-x
		b=j-y
		print(a,b)
		x_front_y_front(b,a)
		time.sleep(3)
	elif((i<x)&(j<y)):
		a=x-i
		b=y-j
		print(a,b)
		x_back_y_back(b,a)
		time.sleep(3)
	elif((i<x)&(j>y)):
		a=x-i
		b=j-y
		print(a,b)
		x_back_y_front(b,a)
		time.sleep(3)
	elif((i>x)&(j<y)):
		a=i-x
		b=y-j
		print(a,b)
		x_front_y_back(b,a)
		time.sleep(3)
	x=i
	y=j
x_back_y_back(y,x)
GPIO.cleanup()

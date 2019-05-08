#!/usr/bin/python

import os, sys
import weedpotato as pre

# Open a file
path = "/home/pi/project/potatodatasets/"
dirs = os.listdir( path )
count =1
# This would print all the files and directories
for imagename in dirs:
	#file=file.split(".")
	#if(len(file)==2 and file[1]=="jpg"):	
	print("image number processing")
	print(count)
	print(imagename)
	pre.main(path,imagename)
	count+=1

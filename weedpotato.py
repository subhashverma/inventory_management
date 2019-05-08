import sys, traceback
import cv2
import os
import re
import numpy as np
import argparse
import string
from plantcv import plantcv as pcv

def main(path,imagename):
	args = {'names':'names.txt', 
			'outdir':'./output-images'}
	#Read image
	img1, path, filename = pcv.readimage(path+imagename,"native")
	#pcv.params.debug=args['debug']
	#img1 = pcv.white_balance(img,roi=(400,800,200,200))
	#img1 = cv2.resize(img1,(4000,2000))
	shift1 = pcv.shift_img(img1, 10, 'top')
	img1 = shift1
	a = pcv.rgb2gray_lab(img1, 'a')
	img_binary = pcv.threshold.binary(a, 120, 255, 'dark')
	fill_image = pcv.fill(img_binary, 10)
	dilated = pcv.dilate(fill_image, 1, 1)
	id_objects, obj_hierarchy = pcv.find_objects(img1, dilated)
	roi_contour, roi_hierarchy = pcv.roi.rectangle(4000, 2000, -2000, -4000 , img1)
	#print(roi_contour)
	roi_objects, roi_obj_hierarchy, kept_mask, obj_area = pcv.roi_objects(img1, 'partial', roi_contour, roi_hierarchy,
			                                                          id_objects, obj_hierarchy)
	clusters_i, contours, hierarchies = pcv.cluster_contours(img1, roi_objects, roi_obj_hierarchy, 1,4)
	'''
	pcv.params.debug = "print"'''
	out = args['outdir']
	names = args['names']
	output_path = pcv.cluster_contour_splitimg(img1, clusters_i, contours, hierarchies, out, file=filename, filenames=names)
if __name__ == '__main__':
	main()

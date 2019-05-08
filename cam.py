import numpy as np
import cv2
import urllib.request as urllib2

url = 'http://192.168.43.1:8080/photo.jpg'

img = urllib2.urlopen(url)
imgnp = np.array(bytearray(img.read()),dtype=np.uint8)
imgg = cv2.imdecode(imgnp,-1)
re_im=cv2.resize(imgg,(4000,2000))
cv2.imwrite("/home/pi/project/potatodatasets/image.jpg", re_im)

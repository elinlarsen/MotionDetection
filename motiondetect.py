#import numpy as np		      # importing Numpy for use w/ OpenCV
import cv2                            # importing Python OpenCV
import time         # importing time for naming files w/ timestamp
#import argparse
import os
import glob

def diffImg(t0, t1, t2):              # Function to calculate difference between images.
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

def motionDetect(path): 
    print ("path  : " + path )
    cam = cv2.VideoCapture(path)
    filename = path
    threshold = 1000                     # Threshold for triggering "motion detection"
    
    # Read three images first:
    t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    #open a file to write inside time with and without mvmt
    file = open(filename+".txt","w")
    file.write("on, off, mvmt \n" )
    # Lets use a time check so we only take 1 pic per sec
    startTime = time.time() #.strftime('%Ss')
    
    #timeCheck = time.time()
    count = 0
    nbframes = cam.get(7)
    mouvement = False
    on = 0.0
    off = 0.0
    print ("number of frames " + str(nbframes))
    #while count < 10:
    while count < (int(nbframes)-4): 
        count +=1
        #print (str(count))
        totalDiff = cv2.countNonZero(diffImg(t_minus, t, t_plus))	# this is total difference number
        ts = cam.get(0) #CAP_PROP_POS_MSEC = 0 get the timestamp in ms
        #print (str(ts))
        if totalDiff >= threshold and mouvement == False : 
            mouvement = True;
            off = ts/1000;
            file.write(str(on)+ "," + str(off)  +",False \n" )
            on = ts/1000;
        elif totalDiff < threshold and mouvement == True :
            mouvement = False;
            off = ts/1000;
            file.write(str(on)+ "," + str(off) + ",True \n" )
            on = ts/1000;
        t_minus = t
        t = t_plus
        t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)       
    runtime = time.time() - startTime
 
      
"""    
path = "/home/lea/Stage/MotionDetection/data/"
for filename in glob.glob(path + '*.mp4'):
    motionDetect(filename)
""" 
motionDetect('/home/lea/Stage/DATA/videos/011100.mp4')     
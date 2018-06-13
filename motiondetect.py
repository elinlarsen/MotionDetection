import numpy as np		      # importing Numpy for use w/ OpenCV
import cv2                            # importing Python OpenCV
from time import time         # importing time for naming files w/ timestamp
import argparse
import time

'''
    TODO :
    - import time of detected motion in video name
    - play with threshold
'''

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
ap.add_argument("-t", "--threshold", type=int, default=120000, help="threshold for triggering motion detection")
args = vars(ap.parse_args())

# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
    cam = cv2.VideoCapture(0)     # Lets initialize capture on webcam
    time.sleep(0.25)

# otherwise, we are reading from a video file
else:
    cam = cv2.VideoCapture(args["video"])
    filename =args["video"]


def diffImg(t0, t1, t2):              # Function to calculate difference between images.
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

threshold = 12000                     # Threshold for triggering "motion detection"

winName = "Movement Indicator"	      # comment to hide window
cv2.namedWindow(winName)              # comment to hide window

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
#open a file to write inside time with and without mvmt
file = open(filename+".txt","w")
file.write("time,mouvement \n" )
# Lets use a time check so we only take 1 pic per sec
startTime = time.time() #.strftime('%Ss')
print ("time.nox = " + str(startTime))
timeCheck = time.time()

while True:
  ret, frame = cam.read()	      # read from camera
  totalDiff = cv2.countNonZero(diffImg(t_minus, t, t_plus))	# this is total difference number
  text = "threshold: " + str(totalDiff)				# make a text showing total diff.
  cv2.putText(frame, text, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)   # display it on screen
  filename = str(time.time() - startTime) 
  if totalDiff > threshold : #and timeCheck != time.time():
    #dimg= cam.read()[1]
    #cv2.imwrite( '_' + filename+ '.jpg', dimg) #time.time().strftime('%Y%m%d_%Hh%Mm%Ss%f')
    file.write(filename + ",true \n" )
  else:
    file.write(filename + ",false \n" )
  timeCheck = time.time()
  # Read next image
  t_minus = t
  t = t_plus
  t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
  cv2.imshow(winName, frame)
  
  key = cv2.waitKey(10)
  if key == 27:			 # comment this 'if' to hide window
    cv2.destroyWindow(winName)
    break
    
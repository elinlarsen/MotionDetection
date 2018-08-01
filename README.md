# MotionDetection
Simple algorithm from Open CV to detect motion in videos, the only parameter here is the threshold. 
For each video a.txt file with the same name will be created containing the motion events.  
We used :
http://www.technicdynamic.com/2017/08/28/python-motion-detection-with-opencv-simple/
https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/

## Prerequisites
This program works with opencv 3.4.1 and python 3

## Run motiondetect
At least you must indicate the name of the folder that contains your videos to analyze. For each video a.txt file with the same name will be created containing the motion events. You can specify the output folder or the threshold. The default thershold is 800.

To run the script with default value :
'''
python motiondetect.py -i '/DATA/videos/tests'
'''
After -i the input folder path(your video folder)

'''
python motiondetect.py -i '/home/lea/Stage/DATA/videos/Rollins/tests' -o '/home/lea/Stage/MotionDetection/data' -t 1200
'''
You can also choose a folder for txt files after -o, and the threshold after -t.

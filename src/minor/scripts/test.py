#!/usr/bin/env python
import rospy
import numpy as np
import cv2
from sensor_msgs.msg import CompressedImage

frames = 0
np_arr = None

def callback(data):
    global frames, np_arr
    np_arr = np.fromstring(data.data, np.uint8)
    image_np = cv2.imdecode(np_arr, 1)
    frames += 1
    print('Processed frame %s' % frames)

rospy.init_node('display')
sub = rospy.Subscriber("camera/image/compressed", CompressedImage, callback)
sub.unregister()
rate = rospy.Rate(10)
print('Done initializing')

while frames < 10:
    rate.sleep()

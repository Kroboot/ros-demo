#!/usr/bin/env python
import cv2
import numpy as np
import rospy
from command import *
from sensor_msgs.msg import CompressedImage


class Camera:
    def __init__(self):
        rospy.init_node('camera')
        rospy.loginfo('%s: connected' % rospy.get_name())
        self.sub = rospy.Subscriber('camera/image/compressed', CompressedImage, self.callback)

    def callback(self, data):
        rospy.loginfo('%s: connected' % rospy.get_name())

        # Read raw image from NumPy array
        np_arr = np.fromstring(data.data, np.uint8)
        image_np = cv2.imdecode(np_arr, 1)
        image_np2 = cv2.imdecode(np_arr, 1)
        rows, cols = image_np.shape[:2]

        # Rotate the image about its origin:
        # - create a rotation matrix
        rotation = cv2.getRotationMatrix2D((cols / 2, rows / 2), -90, 1)

        # - create a translation to the center
        (tx, ty) = ((rows - cols) / 2, (cols - rows) / 2)
        rotation[0, 2] += tx
        rotation[1, 2] += ty

        # - apply matrices
        image_r_np = cv2.warpAffine(image_np, rotation, (rows, cols))

        # Display the result
        cv2.namedWindow('cv_img', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('cv_img', 540, 960)
        cv2.imshow('cv_img', image_r_np)
        cv2.waitKey(2)

    def run(self):
        rospy.spin() # blocking call, after this everything is handled by callbacks
        cv2.destroyAllWindows()

if __name__ == '__main__':
    Camera().run()

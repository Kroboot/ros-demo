#!/usr/bin/env python
import rospy
from threading import Event, Thread
from beginner_tutorials import msg
from command import *


class Display:
    def __init__(self):
        rospy.init_node('display')
        rospy.loginfo("%s: connected" % (rospy.get_name()))
        self.sub = rospy.Subscriber("sensors", msg.Command, self.callback)

    def callback(self, data):
        params = (rospy.get_caller_id(), Command.get(data.c))
        rospy.loginfo("%s: heard %s" % params)


if __name__ == '__main__':
    Display()
    rospy.spin()

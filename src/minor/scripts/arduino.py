#!/usr/bin/env python
import rospy
from threading import Event, Thread
from minor import msg
from command import *


class Arduino:
    def __init__(self):
        # In ROS, nodes are uniquely named. If two nodes with the same
        # node are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('arduino')
        rospy.loginfo('%s: connected' % (rospy.get_name()))
        self.sub = rospy.Subscriber('commands', msg.Command, self.callback)
        self.pub = rospy.Publisher('sensors', msg.Command, queue_size=10)
        self.rate = rospy.Rate(10) # 10hz

    def callback(self, data):
        params = (rospy.get_caller_id(), Command.get(data.c))
        rospy.loginfo('%s: heard %s' % params)

    def run(self, event):
        while not event.wait(0):
            self.pub.publish(Forward().msg())
            self.rate.sleep()


if __name__ == '__main__':
    a = Arduino()

    event = Event()
    thread = Thread(target = a.run, args=(event,))
    thread.start()

    rospy.spin()

    event.set()
    thread.join()

#!/usr/bin/env python
import rospy

from minor.srv import *

class Calculator:
    def __init__(self):
        rospy.init_node('add_two_ints_server')
        rospy.Service('add_two_ints', AddTwoInts, self.handle)
        print('Calculator constructed')

    def run(self):
        print('Ready to add two ints.')
        rospy.spin()

    def handle(self, req):
        return AddTwoIntsResponse(describe(req.a, req.b, self.plus))

    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return plus(a, -b)

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return multiply(a, 1/b)


def describe(a, b, fn):
    print 'Returning [%s %s %s = %s]' % (a, fn.__name__, b, fn(a, b))
    return fn(a, b)


if __name__ == '__main__':
    Calculator().run()

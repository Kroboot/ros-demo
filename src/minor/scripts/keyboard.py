#!/usr/bin/env python
import rospy
from command import *
from minor import msg


def getch():
    import termios
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return _getch()


class Controller:
    cont = True
    commands = {}

    def __init__(self):
        rospy.init_node('controller')
        rospy.loginfo("%s: connected" % rospy.get_name())
        self.pub = rospy.Publisher('commands', msg.Command, queue_size=10)

    def registercb(self, key, cb):
        self.commands[key] = cb

    def register(self, key, command):
        self.registercb(key, lambda: self.send(command.msg()))

    def send(self, command):
        self.pub.publish(command)

    def run(self):
        while self.cont:
            try:
                self.commands[getch()]()
            except KeyError:
                pass

    def quit(self):
        self.cont = False


if __name__ == '__main__':
    c = Controller()
    c.registercb('q', c.quit)
    c.register('w', Forward())
    c.register('s', Backward())
    c.register('a', Left())
    c.register('d', Right())

    try:
        c.run()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/evn python
from beginner_tutorials import msg


class Command():
    cid = None
    commands = {}

    def msg(self):
        return msg.Command(self.cid)

    @staticmethod
    def get(cid):
        return Command.commands[cid].__class__.__name__


class Forward(Command):
    cid = 0
class Backward(Command):
    cid = 1
class Left(Command):
    cid = 2
class Right(Command):
    cid = 3


Command.commands = { c.cid: c for c in [ Forward(), Backward(), Left(), Right() ] }

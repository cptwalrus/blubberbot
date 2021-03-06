import asyncio

from config import Config
from blubberbot import BlubberBot
from message import Message

'''
        Module base class - all modules must provide AT MINIMUM the following:

            self.CALLBACKS = {"!foo": self.foo_impl, "!bar": self.bar_impl }
            self.COOLDOWNS = {"!foo": { "cooldown": <int>, "lastcall": <epoch> }
                ^This is the list of commands your module will respond to, and the associated function that will be called
                simple dictionary in fmt: {"command": function }

            Module name MUST only have the first character uppercase -- sorry.. I don't wanna implement anymore fancy fixes for that

            all commands must
'''
class Module:

    def __init__(self, ctx):

        self.CALLBACKS = {}
        self.COOLDOWNS = {}
        self.ctx = ctx
        self.cfg = ctx.cfg

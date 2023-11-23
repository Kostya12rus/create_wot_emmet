# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/triggers_controller.py
import Event

class TriggersController(object):

    def __init__(self):
        self.__enabled = False
        self.onTrigger = Event.Event()

    def onBecomePlayer(self):
        self.__enabled = True

    def onBecomeNonPlayer(self):
        self.__enabled = False

    def externalTrigger(self, eventId, extra):
        if not self.__enabled:
            return
        self.onTrigger(eventId, extra)

    def handleKey(self, isDown, key, mods):
        pass
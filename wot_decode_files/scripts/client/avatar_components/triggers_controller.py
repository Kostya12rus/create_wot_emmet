# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
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
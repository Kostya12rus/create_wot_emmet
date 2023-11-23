# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/DogTagsInfo.py
import typing, BigWorld, Event
if typing.TYPE_CHECKING:
    from typing import List, Tuple

class DogTagsInfo(BigWorld.DynamicScriptComponent):

    def __init__(self):
        self.__eManager = Event.EventManager()
        self.onUsedComponentsUpdated = Event.Event(self.__eManager)

    def onLeaveWorld(self, *args):
        self.__eManager.clear()

    def setSlice_usedDogTagsComponents(self, changePath, oldValue):
        begin, end = changePath[0]
        newComponents = self.usedDogTagsComponents[begin:end]
        self.onUsedComponentsUpdated(newComponents)
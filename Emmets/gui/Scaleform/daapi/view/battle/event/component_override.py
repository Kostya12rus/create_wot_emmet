# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/component_override.py
from gui.battle_control import avatar_getter
from constants import ARENA_GUI_TYPE

class EventComponentOverride(object):
    __slots__ = ('__usualObject', '__eventObject')

    def __init__(self, usualObject, eventObject):
        super(EventComponentOverride, self).__init__()
        self.__usualObject = usualObject
        self.__eventObject = eventObject

    def __call__(self):
        arena = avatar_getter.getArena()
        isEvent = arena.guiType == ARENA_GUI_TYPE.EVENT_BATTLES if arena else False
        if isEvent:
            return self.__eventObject
        return self.__usualObject
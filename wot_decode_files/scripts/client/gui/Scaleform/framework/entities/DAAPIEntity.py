# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/DAAPIEntity.py
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity

class DAAPIEntity(EventSystemEntity):

    def __init__(self):
        super(DAAPIEntity, self).__init__()
        self.__flashObject = None
        self.__isDAAPIInited = False
        return

    @property
    def flashObject(self):
        return self.__flashObject

    def turnDAAPIon(self, setScript, movieClip):
        if not self.__isDAAPIInited:
            self.__flashObject = movieClip
            if setScript:
                self.__flashObject.script = self
                self.__isDAAPIInited = True

    def turnDAAPIoff(self, isScriptSet):
        if isScriptSet:
            self.__flashObject.script = None
            self.__isDAAPIInited = False
        self.__flashObject = None
        return

    def _isDAAPIInited(self):
        return self.__isDAAPIInited
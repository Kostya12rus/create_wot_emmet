# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventRadialMenuMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventRadialMenuMeta(BaseDAAPIComponent):

    def showHandCursor(self):
        self._printOverrideError('showHandCursor')

    def hideHandCursor(self):
        self._printOverrideError('hideHandCursor')

    def leaveRadialMode(self):
        self._printOverrideError('leaveRadialMode')

    def as_showWithNameS(self, radialState, offset, ratio, targetDisplayName):
        if self._isDAAPIInited():
            return self.flashObject.as_showWithName(radialState, offset, ratio, targetDisplayName)
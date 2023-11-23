# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsViewBaseMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MissionsViewBaseMeta(BaseDAAPIComponent):

    def dummyClicked(self, clickType):
        self._printOverrideError('dummyClicked')

    def as_showDummyS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showDummy(data)

    def as_hideDummyS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideDummy()

    def as_setWaitingVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaitingVisible(visible)

    def as_setBackgroundS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackground(source)
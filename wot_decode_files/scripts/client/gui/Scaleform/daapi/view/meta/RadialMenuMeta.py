# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RadialMenuMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RadialMenuMeta(BaseDAAPIComponent):

    def onSelect(self):
        self._printOverrideError('onSelect')

    def onAction(self, action):
        self._printOverrideError('onAction')

    def onHideCompleted(self):
        self._printOverrideError('onHideCompleted')

    def onRefresh(self):
        self._printOverrideError('onRefresh')

    def as_buildDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_buildData(data)

    def as_showS(self, cursorX, cursorY, radialState, replyStateDiff, offset):
        if self._isDAAPIInited():
            return self.flashObject.as_show(cursorX, cursorY, radialState, replyStateDiff, offset)

    def as_hideS(self, allowAction):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(allowAction)
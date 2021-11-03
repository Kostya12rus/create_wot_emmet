# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
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
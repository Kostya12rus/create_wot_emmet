# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CalloutPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CalloutPanelMeta(BaseDAAPIComponent):

    def onHideCompleted(self):
        self._printOverrideError('onHideCompleted')

    def onHideStart(self):
        self._printOverrideError('onHideStart')

    def as_setDataS(self, action, vehicleType, vehicleName, leftText, rightText, keyText):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(action, vehicleType, vehicleName, leftText, rightText, keyText)

    def as_setHideDataS(self, wasAnswered, answeredAction):
        if self._isDAAPIInited():
            return self.flashObject.as_setHideData(wasAnswered, answeredAction)
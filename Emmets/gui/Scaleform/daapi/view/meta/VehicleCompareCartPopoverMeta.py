# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleCompareCartPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class VehicleCompareCartPopoverMeta(SmartPopOverView):

    def remove(self, id):
        self._printOverrideError('remove')

    def removeAll(self):
        self._printOverrideError('removeAll')

    def gotoCompareView(self):
        self._printOverrideError('gotoCompareView')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()

    def as_updateToCmpBtnPropsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateToCmpBtnProps(data)

    def as_updateClearBtnPropsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateClearBtnProps(data)
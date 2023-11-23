# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleCompareConfiguratorBaseViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehicleCompareConfiguratorBaseViewMeta(BaseDAAPIComponent):

    def applyConfig(self):
        self._printOverrideError('applyConfig')

    def resetConfig(self):
        self._printOverrideError('resetConfig')

    def onCloseView(self):
        self._printOverrideError('onCloseView')

    def as_setResetEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setResetEnabled(value)

    def as_setApplyEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setApplyEnabled(value)

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
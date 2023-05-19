# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionsMapViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PersonalMissionsMapViewMeta(BaseDAAPIComponent):

    def onRegionClick(self, id):
        self._printOverrideError('onRegionClick')

    def as_setPlanDataS(self, planData):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlanData(planData)

    def as_getPmTypeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getPmType()
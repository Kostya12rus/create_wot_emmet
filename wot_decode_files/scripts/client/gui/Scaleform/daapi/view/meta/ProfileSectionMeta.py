# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileSectionMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ProfileSectionMeta(BaseDAAPIComponent):

    def setActive(self, value):
        self._printOverrideError('setActive')

    def requestData(self, vehicleId):
        self._printOverrideError('requestData')

    def requestDossier(self, type):
        self._printOverrideError('requestDossier')

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_responseDossierS(self, battlesType, data, frameLabel, emptyScreenLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_responseDossier(battlesType, data, frameLabel, emptyScreenLabel)
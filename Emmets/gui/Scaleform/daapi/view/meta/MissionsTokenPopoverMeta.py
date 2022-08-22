# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsTokenPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class MissionsTokenPopoverMeta(SmartPopOverView):

    def onQuestClick(self, idx):
        self._printOverrideError('onQuestClick')

    def onBuyBtnClick(self):
        self._printOverrideError('onBuyBtnClick')

    def as_setStaticDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setListDataProviderS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setListDataProvider(data)
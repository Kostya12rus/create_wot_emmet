# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesIntroMeta.py
from gui.Scaleform.framework.entities.View import View

class RankedBattlesIntroMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onAcceptClick(self):
        self._printOverrideError('onAcceptClick')

    def onDetailedClick(self):
        self._printOverrideError('onDetailedClick')

    def onPlayVideoClick(self):
        self._printOverrideError('onPlayVideoClick')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setAlertMessageBlockDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlertMessageBlockData(data)

    def as_setBeforeSeasonBlockDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBeforeSeasonBlockData(data)
# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesPageMeta.py
from gui.Scaleform.framework.entities.View import View

class RankedBattlesPageMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onPageChanged(self, viewId):
        self._printOverrideError('onPageChanged')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)

    def as_setCountersS(self, countersData):
        if self._isDAAPIInited():
            return self.flashObject.as_setCounters(countersData)
# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MapsTrainingBattleLoadingMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MapsTrainingBattleLoadingMeta(BaseDAAPIComponent):

    def gotoBattle(self):
        self._printOverrideError('gotoBattle')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setDataPageS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDataPage(data)

    def as_updateProgressS(self, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgress(percent)
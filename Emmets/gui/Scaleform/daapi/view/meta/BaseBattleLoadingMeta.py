# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseBattleLoadingMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BaseBattleLoadingMeta(BaseDAAPIComponent):

    def as_setProgressS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(value)

    def as_setMapIconS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapIcon(source)

    def as_setEventInfoPanelDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setEventInfoPanelData(data)

    def as_setTipS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTip(value)

    def as_setTipTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTipTitle(title)

    def as_setVisualTipInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisualTipInfo(data)
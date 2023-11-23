# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicBattleUpgradePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EpicBattleUpgradePanelMeta(BaseDAAPIComponent):

    def onSelectItem(self, itemID):
        self._printOverrideError('onSelectItem')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_toggleAlertStateS(self, isVisible, alertText=None):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleAlertState(isVisible, alertText)

    def as_setVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(isVisible)

    def as_showSelectAnimS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelectAnim(idx)

    def as_showNotificationAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showNotificationAnim()

    def as_hideNotificationAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideNotificationAnim()
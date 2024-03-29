# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleDamageLogPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleDamageLogPanelMeta(BaseDAAPIComponent):

    def as_setSettingsDamageLogComponentS(self, isVisible, isColorBlind):
        if self._isDAAPIInited():
            return self.flashObject.as_setSettingsDamageLogComponent(isVisible, isColorBlind)

    def as_summaryStatsS(self, damage, blocked, assist, stun):
        if self._isDAAPIInited():
            return self.flashObject.as_summaryStats(damage, blocked, assist, stun)

    def as_updateSummaryDamageValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryDamageValue(value)

    def as_updateSummaryBlockedValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryBlockedValue(value)

    def as_updateSummaryAssistValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryAssistValue(value)

    def as_updateSummaryStunValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryStunValue(value)

    def as_detailStatsTopS(self, isVisible, isShortMode, messages):
        if self._isDAAPIInited():
            return self.flashObject.as_detailStatsTop(isVisible, isShortMode, messages)

    def as_addDetailMessageTopS(self, value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG):
        if self._isDAAPIInited():
            return self.flashObject.as_addDetailMessageTop(value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG)

    def as_detailStatsBottomS(self, isVisible, isShortMode, messages):
        if self._isDAAPIInited():
            return self.flashObject.as_detailStatsBottom(isVisible, isShortMode, messages)

    def as_addDetailMessageBottomS(self, value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG):
        if self._isDAAPIInited():
            return self.flashObject.as_addDetailMessageBottom(value, actionTypeImg, vehicleTypeImg, vehicleName, shellTypeStr, shellTypeBG)

    def as_isDownCtrlButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isDownCtrlButton(value)

    def as_isDownAltButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isDownAltButton(value)